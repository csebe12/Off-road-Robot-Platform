import pyb
from machine import Pin, UART, I2C
import cmd
import global_variables
import ujson
from ina219 import INA219
from orientate import orientate
from utime import sleep_ms

log_flag = False
debug_flag = False

global servo1, servo2, servo3, servo4, ina

# ADC
adc1 = pyb.ADC(Pin('X8'))
adc2 = pyb.ADC(Pin('X7'))
adc3 = pyb.ADC(Pin('X11'))
adc4 = pyb.ADC(Pin('X12'))
voltage = [0, 0, 0, 0]


# INA219 Wattmeter
def ina_init(i2c):
    global ina
    ina = INA219(0.01, i2c, address=0x45)
    ina.configure()


def servo_init(num):
    global servo1, servo2, servo3, servo4
    # Turns off the uart on the port before servo is initialised
    num = int(num)
    if num == 1:
        servo1 = UART(4, baudrate=9600)
        servo1.deinit()
        servo1 = pyb.Servo(1)
        servo1.angle(0)
    elif num == 2:
        servo2 = UART(4, baudrate=9600)
        servo2.deinit()
        servo2 = pyb.Servo(2)
        servo2.angle(0)
    elif num == 3:
        servo3 = UART(2, baudrate=9600)
        servo3.deinit()
        servo3 = pyb.Servo(3)
        servo3.angle(0)
    elif num == 4:
        servo4 = UART(2, baudrate=9600)
        servo4.deinit()
        servo4 = pyb.Servo(4)
        servo4.angle(0)
    cmd.send_uart("Servo {0:d} is ready\n".format(num), log_flag)


def servo_deinit(num):
    global servo1, servo2, servo3, servo4
    num = int(num)
    try:
        if num == 1:
            del servo1
        elif num == 2:
            del servo2
        elif num == 3:
            del servo3
        elif num == 4:
            del servo4

        cmd.send_uart("Servo {0:d} is disabled".format(num), log_flag)

    except KeyError:
        cmd.send_uart("Servo {0:d} is already disabled".format(num), log_flag)


def servo_move(num, dir):
    if num == 1:
        servo = servo1
    elif num == 2:
        servo = servo2
    elif num == 3:
        servo = servo3
    elif num == 4:
        servo = servo4

    curr_angle = servo.angle()
    if str(dir) == "left":
        servo.angle(curr_angle + 10, 100)
        print("left")
    elif str(dir) == "right":
        servo.angle(curr_angle - 10, 100)
        print("right")


def mpu9250_calibrate():
    cmd.debug("Initial offset values: {}".format(str(global_variables.imu.mag.cal)), debug_flag)
    cmd.send_uart("Initial offset values: {}".format(str(global_variables.imu.mag.cal)), log_flag)
    cmd.debug("Rotate robot about each axis then press the Pyboard switch", debug_flag)
    cmd.send_uart("Rotate robot about each axis then press the Pyboard switch", log_flag)
    sw = pyb.Switch()
    global_variables.imu.mag.calibrate(sw)
    cmd.debug("Calibrated offset values are: {}".format(str(global_variables.imu.mag.cal)), debug_flag)
    cmd.send_uart("Calibrated offset values are: {}".format(str(global_variables.imu.mag.cal)), log_flag)


# Mag is a blocking read and it takes 10ms
def mpu9250_read():
    while True:
        global_variables.imu_acc = global_variables.imu.accel.xyz
        global_variables.imu_gyr = global_variables.imu.gyro.xyz
        global_variables.imu_mag = global_variables.imu.mag.xyz


def mag_read():
    return global_variables.imu.mag.xyz


def fusion_calibrate():
    global_variables.pid_test.stop_update()
    cmd.debug("Calibrating fusion", debug_flag)
    cmd.send_uart("Calibrating fusion", log_flag)
    cmd.send_uart("Rotate robot about each axis then press the Pyboard switch", log_flag)
    sw = pyb.Switch()
    global_variables.fuse.calibrate(mag_read, sw, lambda:pyb.delay(100))
    cmd.debug("Calibration done: {}".format(global_variables.fuse.magbias), debug_flag)
    cmd.send_uart("Calibration done {}".format(global_variables.fuse.magbias), log_flag)
    global_variables.pid_test.start_update()


def fusion_read():
    i = 0
    while True:
        if i % 7 == 0:
            sleep_ms(1)
            acc = global_variables.imu.accel.xyz
            gyr = global_variables.imu.gyro.xyz
            mag = global_variables.imu.mag.xyz
        global_variables.fuse.update(acc, gyr, mag)  # Note blocking mag read


def cell_voltage():
    voltage[0] = round((adc1.read()/4095) * 5.16, 2)
    voltage[1] = round((adc2.read()/4095) * 5.16, 2)
    voltage[2] = round((adc3.read()/4095) * 5.16, 2)
    voltage[3] = round((adc4.read()/4095) * 5.16, 2)

    return voltage


def send_voltage():
    voltage = cell_voltage()
    msg = {"type": "battery", "1": str(voltage[0]), "2": str(voltage[1]), "3": str(voltage[2]), "4": str(voltage[3])}
    msg = ujson.dumps(msg)
    cmd.send_uart(msg, log_flag)
    lowest = min(voltage)
    if 3.2 >= lowest > 3.0:
        if debug_flag is True:
            cmd.debug("Critical level: cell {0}".format(str((voltage.index(lowest) + 1))), debug_flag)
        cmd.send_uart("Critical level: cell {0}".format(str((voltage.index(lowest) + 1))), log_flag)
    elif 3.0 >= lowest > 1:
        if debug_flag is True:
            cmd.debug("Battery dead: cell {0}".format(str((voltage.index(lowest) + 1))), debug_flag)
        cmd.send_uart("Battery dead: cell {0}".format(str((voltage.index(lowest) + 1))), log_flag)


def motor_current():
    voltage = ina.voltage()
    current = ina.current()
    power = ina.power()
    msg = {"type": "motor_current", "voltage": str(round(voltage, 2)), "current": str(round(current, 2)),
           "power": str(round(power, 2))}
    msg = ujson.dumps(msg)

    cmd.send_uart(msg, log_flag)