import board
import neopixel
import RPi.GPIO as GPIO
import time
import comms
import board_restarts


def init():
	global uart
	global socketio
	global cmd_history
	global pwr_ratio
	global ping_counter
	global np
	global np_curr_color
	global np_alt_color
	global np_duty
	global np_freq
	global switch_state
	global switch_start_time
	global switch_end_time
	global elapsed
	global time_flag
	global user_connected
	global log, mag_read, gps_log

	cmd_history = []
	cmd_history.clear()
	pwr_ratio = 0.3
	ping_counter = 0

	np = neopixel.NeoPixel(board.D12, 1, auto_write=False, pixel_order=neopixel.RGB)
	np_curr_color = (0,0,0)
	np_alt_color = (0,0,0)
	np_duty = 0
	np_freq = 1


	GPIO.setmode(GPIO.BCM)
	GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(25, GPIO.BOTH, callback=switch, bouncetime=200)
	switch_state = False
	elapsed = 0
	switch_start_time = 0
	switch_end_time = 0
	time_flag = False
	user_connected = False



def switch(channel):
	global switch_state, switch_start_time, switch_end_time, elapsed, time_flag
	# The interrupt is called on both edges. This variable will be true when the
	# toggle switch is held in position. This can be used to determine the time
	# period for which the switch was held pressed
	switch_state = not switch_state

	# # Toggle pressed
	if switch_state is True:
		switch_start_time = time.time()
		print("pressed")
		time_flag = False
	# Toggle released
	else:
		# If it is 1, it is in the correct state
		time.sleep(0.05)
		check = GPIO.input(channel)
		if check == 1:
			switch_end_time = time.time()
			print("depressed")
			if switch_start_time != 0:
				time_flag = True
				elapsed = switch_end_time - switch_start_time
				switch_start_time = 0
				switch_end_time = 0
		else:
			print("error")
			switch_state = not switch_state
			switch_start_time = 0
			switch_end_time = 0
			time_flag = False

	if time_flag is True:
		if elapsed < 5:
			comms.send_command("reset/soft")
		elif (elapsed >= 5) and (elapsed < 10):
			board_restarts.rpi_shutdown()
		elif (elapsed >= 10) and (elapsed < 15):
			board_restarts.rpi_restart()

# Colors, duty_cycle
def led_thread():
	global np_duty, np_freq, np_alt_color, np_curr_color, np, switch_start_time

	while True:
		# Led modes when the toggle is pressed down
		if switch_start_time != 0:
			np_duty = 100
			np_freq = 1
			elapsed = time.time() - switch_start_time
			print
			if elapsed < 5:
				np_curr_color = (0, 0, 255)
			elif (elapsed >= 5) and (elapsed < 10):
				np_curr_color = (255,0,0)
			elif (elapsed >= 10) and (elapsed < 15):
				np_curr_color = (0,0,0)
			else:
				np_curr_color = (40, 110, 222)
				np_duty = 50
				np_freq = 2

		sleep_primary = (np_duty/100)*(1/np_freq)
		sleep_secondary = ((100-np_duty)/100)*(1/np_freq)
		if sleep_primary != 0:
			np.fill(np_curr_color)
			np.show()
			time.sleep(sleep_primary)
		if sleep_secondary != 0:
			np.fill(np_alt_color)
			np.show()
			time.sleep(sleep_secondary)

# Duty is between 0-100, color is an RGB tuple
# If it is called without any color arguments, it will only light in the previous state continuously
def led(freq=1, duty=50, color=-1, alternate_color=-1):
	global np_duty, np_freq, np_alt_color, np_curr_color
	# Only update parameters if there is a change
	if color != np_curr_color:
		if color != -1:
			np_curr_color = color
	if alternate_color != np_alt_color:
		if alternate_color != -1:
			np_alt_color = alternate_color
	if duty != np_duty:
		np_duty = duty
	if freq != np_freq:
		np_freq = freq




