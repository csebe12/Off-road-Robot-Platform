import comms
from time import sleep

def console_input():
	print("----------------------------------------------")
	print("| Enter your command manually then hit enter |")
	print("----------------------------------------------")
	while True:
		send = input()
		comms.send_command(send)
		
