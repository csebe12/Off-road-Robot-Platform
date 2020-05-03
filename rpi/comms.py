import serial
import sys
sys.path.insert(1, '/home/pi/Desktop/app')
import global_vars
import web_server
import time
import json


def uart_init():
    # Use ttyAMA0 on RPi 3, S0 on RPi zero w
    #uart = serial.Serial('/dev/ttyS0',38400) # if it doesn't work try ttyAMA0
    global_vars.uart = serial.Serial('/dev/ttyS0', 38400, timeout=2) # if it doesn't work try ttyAMA0
    print('Serial open')


def uart_close():
    global_vars.uart.close()
    print('\nSerial closed') 
        
def log_init():
    global_vars.log = open("/home/pi/Desktop/log.txt", "a")
    global_vars.log.write("---\n")
    print("Log file opened\n")
    global_vars.mag_read = open("/home/pi/Desktop/mag_read.csv", "w")
    print("Mag read file opened\n")
    global_vars.gps_log = open("/home/pi/Desktop/gps_log.txt", "a")
    global_vars.gps_log.write("---\n")
    print("GPS log opened\n")
    
def log_close():
    global_vars.log.close()
    print("Log file closed\n")
    global_vars.mag_read.close()
    print("Mag read file closed\n")
    global_vars.gps_log.close()
    print("GPS log closed\n")
        
def uart_read():
    cmd = global_vars.uart.readline()
    if cmd is not None:
        if len(cmd) > 0:
            cmd = cmd.decode()
            print('Incoming: ', cmd)
            data = cmd.split('/')

            if data[0] == 'l':
                global_vars.log.write(data[1])
            elif data[0] == 'mag':
                global_vars.mag_read.write(data[1])
            elif data[0] != 'm_a_j':
                web_server.uart_cmd(['pyb', cmd])
            # Save gps history to log file
            try:
                json_msg = json.loads(cmd)
                if json_msg["func"] == "position":
                    lat = json_msg["lat"]
                    lon = json_msg["long"]
                    if lat != "None" and lon != "None":
                        global_vars.gps_log.write("lat: {0}, lon: {1}\n".format(lat, lon))
            except (ValueError, KeyError):
                pass

def send_command(cmd, display=True):
    if cmd[-1] is not '\n':
        cmd = cmd + "\n"
    global_vars.uart.write(cmd.encode('utf-8'))
    print("Command sent: " + cmd)
    # Sending cmd to front-end
    if display is True:
        web_server.uart_cmd(['rpi', cmd])

def ping():
    loop_counter = 0
    while True:
        if global_vars.user_connected is True:
            if (loop_counter % 3) == 0:
                send_command("ping/", False)
                time.sleep(1)
            send_command("gps/status", False)
            time.sleep(5)
            send_command("planner/status", False)
            time.sleep(2)
            send_command("sensors/motor_current", False)
            time.sleep(2)
            if (loop_counter % 7) == 0:
                send_command("sensors/battery", False)
                time.sleep(1)
            loop_counter = loop_counter + 1   
        global_vars.ping_counter += 1
        if global_vars.ping_counter > 6:
            global_vars.socketio.emit('ping', False, namespace='/signals')

