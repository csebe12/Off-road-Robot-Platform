import machine
from utime import sleep_ms

while True:
	sleep_ms(3000)
	machine.reset()