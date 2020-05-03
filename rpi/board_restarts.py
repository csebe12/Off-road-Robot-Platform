from subprocess import call
import comms
import global_vars
import web_server
import time

def rpi_restart():
	print("restart")
	web_server.uart_cmd(['rpi', "RPi restart"])
	comms.uart_close()
	comms.log_close()
	global_vars.led(color=(255,255,255), alternate_color=(0,0,0), freq=2)
	time.sleep(5)
	global_vars.led(color=(255,255,255), duty=100)
	time.sleep(3)
	global_vars.np.deinit()
	call("sudo shutdown -r now", shell=True)

def rpi_shutdown():
	print("shutdown")
	web_server.uart_cmd(['rpi', "RPi shutdown"])
	comms.uart_close()
	comms.log_close()
	global_vars.led(color=(255,0,0), alternate_color=(0,0,0), freq=2)
	time.sleep(5)
	global_vars.led(color=(255,0,0),duty=100)
	time.sleep(3)
	global_vars.np.deinit()
	call("sudo shutdown -h now", shell=True)
