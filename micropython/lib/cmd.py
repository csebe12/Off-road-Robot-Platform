import utime
import motor
import global_variables
import sensors
import _thread
import machine
import ujson

log_flag = False
debug_flag = False

if log_flag is True:
    log = 'l/'
else:
    log = ''


def send_uart(message, flag):
    try:
        message = message.decode()
    except (UnicodeError, AttributeError):
        pass

    if (global_variables.UART_comms_master is True) or (flag is True):
        if message[-1] != '\n':
            message = message + '\n'
        msg = log + message
        global_variables.uart.write(msg.encode('utf-8'))


def debug(messages, flag):
    if flag is True:
        if type(messages) == tuple:
            for message in messages:
                global_variables.uart.write(str(message).encode('utf-8'))
                print(str(message))
        else:
            global_variables.uart.write(str(messages).encode('utf-8'))
            print(str(messages))


def read_uart():
    data = global_variables.uart.readline()

    if data is not None:
        data = data.decode()
    else:
        data = 'no msg'

    return data


def command():
    # Flag for incorrect command
    incorrect_cmd = False

    messages = read_uart()
    # Splits up multiple commands in the buffer
    messages = messages.split('\n')

    # Delete empty commands
    if len(messages[-1]) == 0:
        del messages[-1]

    for message in messages:
        message.strip()

        if message == "stop":
            stop()

        message = message.split('/')
        # If there is no separator (invalid input), length will be 1
        if len(message) > 1:
            cmd_type = message[0]
            command = message[1]

            # Absolute motor command
            # m_a/l,10,r,-43
            # m_a_j is only used by the joystick and is used
            # to suppress displaying motor command messages on front end
            if (cmd_type == 'm_a') or (cmd_type == 'm_a_j'):
                command = command.split(',')
                # Single side motor command needs 2 arguments. If less/more are given, it raises the flag
                if len(command) == 2:
                    flag = command_verify((command[0], command[1]))
                    # Correct command
                    if flag[0] is False:
                        if debug_flag is True:
                            debug((str(command[0]), int(command[1])), debug_flag)
                        motor.motor_abs((str(command[0]), int(command[1])))
                        if cmd_type == 'm_a':
                            send_uart(cmd_type + "/ valid input\n", log_flag)
                    else:
                        incorrect_cmd = True
                        error_msg = flag[1]
                # Double side motor command needs 4 arguments. If less/more are given, it raises the flag
                elif len(command) == 4:
                    flag = command_verify((command[0], command[1]), (command[2], command[3]))
                    # Correct command
                    if flag[0] is False:
                        if debug_flag is True:
                            debug((str(command[0]), int(command[1]), str(command[2]), int(command[3])), debug_flag)
                        motor.motor_abs((str(command[0]), int(command[1])), (str(command[2]), int(command[3])))
                        if cmd_type == 'm_a':
                            send_uart(cmd_type + "/ valid input\n", log_flag)
                    else:
                        incorrect_cmd = True
                        error_msg = flag[1]
                else:
                    incorrect_cmd = True
                    error_msg = 'Incorrect number of motor arguments\n'

            # Relative motor command
            # m_r/l,-4,r,32
            elif cmd_type == 'm_r':
                command = command.split(',')
                if len(command) == 2:
                    flag = command_verify((command[0], command[1]))
                    # Correct command
                    if flag[0] is False:
                        if debug_flag is True:
                            debug((str(command[0]), int(command[1])), debug_flag)
                        rel_flag = motor.motor_rel((str(command[0]), int(command[1])))
                        if rel_flag[0] is False:
                            send_uart("valid input\n", log_flag)
                        else:
                            send_uart(rel_flag[1], log_flag)
                    else:
                        incorrect_cmd = True
                        error_msg = flag[1]
                elif len(command) == 4:
                    flag = command_verify((command[0], command[1]), (command[2], command[3]))
                    # Correct command
                    if flag[0] is False:
                        if debug_flag is True:
                            debug((str(command[0]), int(command[1]), str(command[2]), int(command[3])), debug_flag)
                        rel_flag = motor.motor_rel((str(command[0]), int(command[1])), (str(command[2]), int(command[3])))
                        if rel_flag[0] is False:
                            send_uart("valid input\n", log_flag)
                        else:
                            send_uart(rel_flag[1], log_flag)
                    else:
                        incorrect_cmd = True
                        error_msg = flag[1]

            # PID
            # pid/start, pid/stop, pid/set_pid(P,I,D), pid/set_pwr(MAXPOWER), pid/get_pid, pid/get_pwr
            elif cmd_type == 'pid':
                command = command.split('(')
                if command[0] == 'start':
                    _thread.start_new_thread(global_variables.pid_thread, ())
                elif command[0] == 'stop':
                    global_variables.pid_test.stop_update()
                elif command[0] == 'set_pid':
                    end = command[1].find(')')
                    if end is not -1:
                        command = command[1][0:end]
                        command = command.split(',')
                        try:
                            p = float(command[0])
                            i = float(command[1])
                            d = float(command[2])
                            global_variables.pid_test.set_pid(p, i, d)
                            send_uart("PID coefficients set", log_flag)
                        except ValueError:
                            error_msg = 'invalid PID'
                            incorrect_cmd = True
                elif command[0] == 'get_pid':
                    (Kp, Ki, Kd) = global_variables.pid_test.get_pid()
                    send_uart("Kp: {0:.2f} Ki: {1:.2f} Kd: {2:.2f}".format(Kp, Ki, Kd), log_flag)
                elif command[0] == 'set_pwr':
                    end = command[1].find(')')
                    if end is not -1:
                        try:
                            pwr = float(command[1][0:end])
                            flag = global_variables.pid_test.set_pwr(pwr)
                            if flag is True:
                                send_uart("PID power limit is: {0:.2f}".format(pwr), log_flag)
                            else:
                                send_uart("PID power limit out of range", log_flag)
                        except ValueError:
                            error_msg = 'invalid PID power'
                            incorrect_cmd = True
                elif command[0] == 'get_pwr':
                    send_uart("PID power limit is: {0:.2f}".format(global_variables.pid_test.get_pwr()), log_flag)
                else:
                    incorrect_cmd = True
                    error_msg = 'Invalid PID command'

            # Reset
            # reset/soft, reset/hard
            elif cmd_type == 'reset':
                if command == 'soft':
                    send_uart("soft reset\n", log_flag)
                    utime.sleep_ms(300)
                    machine.soft_reset()
                elif command == 'hard':
                    send_uart("hard reset\n", log_flag)
                    utime.sleep_ms(300)
                    machine.reset()
                else:
                    incorrect_cmd = True
                    error_msg = 'Invalid reset'

            # GPS
            # gps/status, gps/read, gps/update
            elif cmd_type == 'gps':
                if command == 'status':
                    global_variables.gps_device.gps_data()
                elif command == 'read':
                    global_variables.gps_device.print_msg()
                elif command == 'update':
                    global_variables.gps_device.update()
                else:
                    error_msg = "Invalid gps command"
                    incorrect_cmd = True

            # Planner
            # planner/init, planner/start, planner/stop, planner/status, planner/pause, planner/add_start, planner/coord:[[-43.23, 233],[23.43, 234.4]]
            elif cmd_type == 'planner':
                command = command.split(':')
                if command[0] == 'init':
                    global_variables.gps_planner.waypoint_init()
                elif command[0] == 'add_start':
                    global_variables.gps_planner.waypoint_add(True)
                elif command[0] == 'add_end':
                    global_variables.gps_planner.waypoint_add(False)
                elif command[0] == 'coord':
                    coord = command[1].split(',')
                    global_variables.gps_planner.waypoint_coord(coord)
                elif command[0] == 'start':
                    global_variables.gps_planner.start_planner()
                elif command[0] == 'pause':
                    global_variables.gps_planner.pause_planner()
                elif command[0] == 'resume':
                    global_variables.gps_planner.resume_planner()
                elif command[0] == 'stop':
                    global_variables.gps_planner.stop_planner()
                elif command[0] == 'home':
                    global_variables.gps_planner.go_home()
                elif command[0] == 'status':
                    global_variables.gps_planner.planner_data()
                else:
                    error_msg = "Invalid planner command"
                    incorrect_cmd = True

            # UART_comms_master
            # uart/on, uart/off
            elif cmd_type == 'uart':
                if command == 'on':
                    global_variables.UART_comms_master = True
                    send_uart("UART on", log_flag)
                elif command == 'off':
                    send_uart("UART off", log_flag)
                    global_variables.UART_comms_master = False
                else:
                    error_msg = "Invalid UART command"
                    incorrect_cmd = True

            # Ping
            # ping/
            elif cmd_type == 'ping':
                backup = global_variables.UART_comms_master
                global_variables.UART_comms_master = True
                send_uart("ping", log_flag)
                global_variables.UART_comms_master = backup

            # Calibrate
            # calibrate/
            elif cmd_type == 'calibrate':
                sensors.fusion_calibrate()

            # Sensors
            # sensors/battery
            elif cmd_type == 'sensors':
                if command == 'battery':
                    sensors.send_voltage()
                elif command == 'motor_current':
                    sensors.motor_current()
                else:
                    error_msg = "Invalid sensor command"
                    incorrect_cmd = True

            # Servo
            # servo/setup-1
            elif cmd_type == 'servo':
                command = command.split('-')
                if command[0] == 'init':
                    sensors.servo_init(command[1])
                elif command[0] == 'move':
                    args = command[1].split(',')
                    sensors.servo_move(int(args[0]), str(args[1]))
                elif command[0] == 'deinit':
                    sensors.servo_deinit(command[1])
                else:
                    error_msg = "Invalid servo command"
                    incorrect_cmd = True

            # --------------------------
            # Must be below all commands
            else:
                incorrect_cmd = True
                error_msg = 'Incorrect first letter in command\n'

            if incorrect_cmd is True:
                send_uart(error_msg, log_flag)
                # Resetting the flag
                incorrect_cmd = False

        else:
            if message[0] == 'stop':
                stop()
            elif message[0] != 'no msg':
                error_msg = 'Invalid input: {}, no separator'.format(str(message))
                send_uart(error_msg, log_flag)


def command_verify(*commands):
    # If incorrect values are given, flag is set True
    # or statements prevent the flag from being overwritten
    # without them if the pwr value is invalid but the side value is correct,
    # the command would pass as valid, although it is invalid
    error_msg = 'Correct parameters'
    incorrect_cmd = False

    for command in commands:
        if len(command) == 2:
            side = command[0]
            try:
                pwr = int(command[1])
            except ValueError:
                incorrect_cmd = incorrect_cmd or True
                error_msg = 'Power not an int\n'
                pwr = 0

            # Power
            if int(pwr) > 100 or int(pwr) < -100:
                pwr = 0
                incorrect_cmd = incorrect_cmd or True
                error_msg = 'Invalid power value\n'

            # Side
            if side == 'l' or side == 'r':
                incorrect_cmd = incorrect_cmd or False
            else:
                incorrect_cmd = incorrect_cmd or True
                error_msg = 'Incorrect side\n'

            if incorrect_cmd is True:
                break
    return incorrect_cmd, error_msg


def stop():
    motor.motor_abs(("l", 0), ("r", 0))
    global_variables.gps_planner.stop_planner()
    send_uart("stop\n", log_flag)