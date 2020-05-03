#!/usr/bin/env python3
import threading
import sys
from signal import signal, SIGINT
sys.path.insert(1, '/home/pi/Desktop/app')
import web_server
import comms
import console
import global_vars
from time import sleep


def handler(signal_received, frame):
	print("\nCtrl + C detected, closing files")
	comms.uart_close()
	comms.log_close()
	global_vars.np.deinit()

	exit(0)

def server_uart():
	try:
		comms.uart_init()
		comms.log_init()
		web_server.server()
	finally:
		comms.uart_close()
		comms.log_close()
		global_vars.np.deinit()

def main():
	signal(SIGINT, handler)

	global_vars.init()
	server_thread = threading.Thread(target=server_uart, args=())
	console_thread = threading.Thread(target=console.console_input, args=())
	ping_thread = threading.Timer(3, comms.ping)
	led_thread = threading.Thread(target=global_vars.led_thread, args=())
	
	server_thread.start()
	console_thread.start()
	ping_thread.start()
	led_thread.start()
	global_vars.led(freq=1, color=(40, 110, 222), alternate_color=(40, 110, 222))
	while True:
		comms.uart_read()
	
	
if __name__ == "__main__":
	main()
