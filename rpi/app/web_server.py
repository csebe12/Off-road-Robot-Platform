# guide to Flask:
# https://pythonhow.com/add-css-to-flask-website/
import comms
import board_restarts
import global_vars
import os
import math
import json
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, redirect, request, Response, make_response
from flask_cors import CORS
import folium

from camera_pi import Camera

def arcade_mixing_function(x_val, y_val):
  l_pwr = int(y_val) + int(x_val)
  r_pwr = int(y_val) - int(x_val)

  max_speed = round(100*global_vars.pwr_ratio)
  min_speed = round(-100*global_vars.pwr_ratio)

  # Clip values if necessary
  if l_pwr > max_speed:
    l_pwr = max_speed
  elif l_pwr < min_speed:
    l_pwr = min_speed
  if r_pwr > max_speed:
    r_pwr = max_speed
  elif r_pwr < min_speed:
    r_pwr = min_speed

  command = "m_a_j/l," + str(l_pwr) + ",r," + str(r_pwr) + "\n"
  comms.send_command(command, False)


def uart_cmd(msg):
  try:
    json_msg = json.loads(msg[1])
    if json_msg["func"] == "position":
      hdop = float(json_msg["hdop"])
      if hdop <= 5:
        global_vars.led(alternate_color=(42, 40, 128), freq=0.5)
      else:
        global_vars.led(alternate_color=(40, 110, 222),color=(40, 110, 222), freq=0.5)
    elif json_msg["func"] == "planner":
      status = json_msg["stat"]
      if status == "Start":
        global_vars.led(color=(76, 175, 80), freq=0.5)
      elif status == "Pause":
        global_vars.led(color=(255, 140, 0), freq=0.5)
      else:
        global_vars.led(alternate_color=(40, 110, 222),color=(40, 110, 222), freq=0.5)

    global_vars.cmd_history.append(msg)
    global_vars.socketio.emit('new_msg', msg, namespace='/signals')

  except (ValueError, KeyError):
    if msg[1] == 'ping' or msg[1] == 'ping\n':
      global_vars.socketio.emit('ping', True, namespace='/signals')
      global_vars.ping_counter = 0
    else:
      global_vars.cmd_history.append(msg)
      global_vars.socketio.emit('new_msg', msg, namespace='/signals')


def server():
  app = Flask(__name__)
  CORS(app)
  global_vars.socketio = SocketIO(app, async_mode=None, logger=False, engineio_logger=False)

  @app.route("/")
  def index():
    return render_template('command_history.html', commands=global_vars.cmd_history)
    
  def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

  @app.route('/video_feed')
  def video_feed():
      """Video streaming route. Put this in the src attribute of an img tag."""
      return Response(gen(Camera()),
                      mimetype='multipart/x-mixed-replace; boundary=frame')


  @app.route("/command")
  def command():
    command = request.args.get("cmd")
    if type(command) is not None:
      comms.send_command(command)
      cmd = command.split('/')
      if cmd[0] == "planner":
        global_vars.gps_log.write(command+'\n')
    
    return command
    # return render_template('command_history.html', commands=global_vars.cmd_history)


  @app.route("/set_speed")
  def set_speed():
    x = request.args.get("x")
    y = request.args.get("y")
    arcade_mixing_function(x,y)
    return x,y

  @app.route("/stop")
  def stop():
    comms.send_command("stop")
    return "stop"

  @app.route("/pwr_ratio")
  def pwr_ratio():
    mode = request.args.get("mode")
    if mode == '0':
      global_vars.pwr_ratio = 0.4
    elif mode == '1':
      global_vars.pwr_ratio = 0.5
    elif mode == '2':
      global_vars.pwr_ratio = 0.7
    return mode

  @app.route("/restarts")
  def restarts():
    mode = request.args.get("mode")
    # Restart pi
    if mode == '0':
      board_restarts.rpi_restart()
    # Shutdown pi
    elif mode == '1':
      board_restarts.rpi_shutdown()
    # Restart pyb
    elif mode == '2':
      comms.send_command("reset/soft")
    elif mode == '3':
      comms.send_command("calibrate/")
    elif mode == '4':
      comms.send_command("uart/on")
    return mode

  @app.route("/servo")
  def servo():
    servo_num = str(request.args.get("num"))
    func = str(request.args.get("func"))
    if func == "init":
      comms.send_command("servo/init-" + servo_num)
    elif func == "move":
      comms.send_command("servo/move-" + servo_num + "," + request.args.get("dir"))
    elif func == "deinit":
      comms.send_command("servo/deinit-" + servo_num)
    return "servo"

  @app.route("/nav")
  def nav():
    func = str(request.args.get("func"))
    global_vars.gps_log.write(func+'\n')
    if func == "start":
      comms.send_command("planner/start")
    elif func == "pause":
      comms.send_command("planner/pause")
    elif func == "stop":
      comms.send_command("planner/stop")
    elif func == "home":
      comms.send_command("planner/home")
    return "nav"




  # @app.route("/set_speed_l")
  # def set_speed_l():
  #   speed_l = request.args.get("speed_l")
  #   print("Left " + str(speed_l))
  #   command_generator('l', speed_l)
  #   return speed_l

  # @app.route("/set_speed_a")
  # def set_speed_a():
  #   speed_a = request.args.get("speed_a")
  #   print("Both " + str(speed_a))
  #   command_generator('a', speed_a)
  #   return speed_a

  # @app.route("/set_speed_r")
  # def set_speed_r():
  #   speed_r = request.args.get("speed_r")
  #   print("Right " + str(speed_r))
  #   command_generator('r', speed_r)
  #   return speed_r
    

  # app.run(host='0.0.0.0', port=5000, threaded=True)
  global_vars.socketio.run(app, host='0.0.0.0', port=5000)