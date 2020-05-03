from pyb import Pin, Timer
import cmd

debug_flag = False

# Initialising motor
# Y3, TIM10, ch1    pwr_left
# Y4, TIM11, ch1    pwr_right
# Y5                dir_left
# Y6                dir_right
p_motor_left = Pin('Y3')
motor_timer_left = Timer(10, freq=5000)
motor_power_left = motor_timer_left.channel(1, Timer.PWM, pin=p_motor_left, pulse_width_percent=0)

p_motor_right = Pin('Y4')
motor_timer_right = Timer(11, freq=5000)
motor_power_right = motor_timer_right.channel(1, Timer.PWM, pin=p_motor_right, pulse_width_percent=0)

motor_direction_left = Pin('Y5', Pin.OUT_PP)
motor_direction_right = Pin('Y6', Pin.OUT_PP)


def motor_abs(*commands):
    for command in commands:
        pwr = command[1]
        if debug_flag is True:
            cmd.debug("side: {0} pwr: {1}".format(str(command[0]), str(pwr)), debug_flag)
        # Forward
        if pwr >= 0:
            direction = True
        # Backward
        elif pwr < 0:
            direction = False
            # pulse_width has to be positive
            pwr = -1*pwr

        if command[0] == "l":
            motor_direction_left.value(direction)
            motor_power_left.pulse_width_percent(pwr)
        elif command[0] == "r":
            motor_direction_right.value(direction)
            motor_power_right.pulse_width_percent(pwr)


def motor_rel(*commands):
    flag = False
    error_msg = 'Correct rel motor command'
    for command in commands:
        delta_pwr = command[1]
        if command[0] == "l":
            current_pwr = motor_power_left.pulse_width_percent()
            current_dir = motor_direction_left.value()
            if current_dir is 0:
                current_pwr = -1*current_pwr
            new_pwr = int(current_pwr + delta_pwr)
            current_pwr_sign = True if current_pwr >= 0 else False
            new_pwr_sign = True if new_pwr >= 0 else False
            # Change the direction of rotation if change_dir is True
            change_dir = current_pwr_sign ^ new_pwr_sign
            new_pwr = abs(new_pwr)

            if (100 >= new_pwr) and (new_pwr >= 0):
                if change_dir is 1:
                    motor_direction_left.value(not current_dir)
                motor_power_left.pulse_width_percent(new_pwr)
                flag = False
            elif new_pwr > 100:
                new_pwr = 100
                if change_dir is 1:
                    motor_direction_left.value(not current_dir)
                motor_power_left.pulse_width_percent(new_pwr)
                flag = True
                error_msg = 'Rel command clipping at 100%, left'

        elif command[0] == "r":
            current_pwr = motor_power_right.pulse_width_percent()
            current_dir = motor_direction_right.value()
            if current_dir is 0:
                current_pwr = -1*current_pwr
            new_pwr = int(current_pwr + delta_pwr)
            current_pwr_sign = True if current_pwr >= 0 else False
            new_pwr_sign = True if new_pwr >= 0 else False
            # Change the direction of rotation if change_dir is True
            change_dir = current_pwr_sign ^ new_pwr_sign
            new_pwr = abs(new_pwr)

            if (100 >= new_pwr) and (new_pwr >= 0):
                if change_dir is 1:
                    motor_direction_right.value(not current_dir)
                motor_power_right.pulse_width_percent(new_pwr)
                flag = False
            elif new_pwr > 100:
                new_pwr = 100
                if change_dir is 1:
                    motor_direction_right.value(not current_dir)
                motor_power_right.pulse_width_percent(new_pwr)
                flag = True
                error_msg = 'Rel command clipping at 100%, right'
        if debug_flag is True:
            cmd.debug("Current pwr: {0} {1:d}".format(str(command[0]), new_pwr), debug_flag)
    return flag, error_msg


# Returns current motor parameters
def get_motor():
    dir_l = motor_direction_left.value()
    dir_r = motor_direction_right.value()
    pwr_l = motor_power_left.pulse_width_percent()
    pwr_r = motor_power_right.pulse_width_percent()
    if dir_l is False:
        pwr_l = -1*pwr_l
    if dir_r is False:
        pwr_r = -1*pwr_r
    return pwr_l, pwr_r