import gps
import planner
import cmd
from machine import UART, I2C, Pin
import pyb
import imu
from mpu9250 import MPU9250
from fusion import Fusion
import pid
import sensors
import gc
from utime import sleep_ms

log_flag = False


def init():
    global uart
    # Initialising UART6 (Y1, Y2)
    uart = UART(6, baudrate=38400, timeout=10, read_buf_len=200)
    pyb.repl_uart(uart)
    print('RPi UART setup')

    global uart_gps
    global gps_device
    global gps_planner
    uart_gps = UART(4, baudrate=9600, timeout=10, read_buf_len=600)
    gps_device = gps.GPS(uart_gps)
    gps_planner = planner.PLANNER(gps_device)
    print("GPS set up")

    global pid_test
    pid_test = pid.PID(0.3, 0, 0.1, gps_planner.dist_bearing, 1)

    # If True, uart messages are sent back normally,
    # if false, only log messages are sent back.
    global UART_comms_master
    UART_comms_master = False

    global imu, fuse, i2c
    global imu_acc, imu_gyr, imu_mag

    i2c = I2C(scl=Pin('Y9'), sda=Pin('Y10'))
    try:
        imu = MPU9250(i2c,scaling=(-1,-1,-1))
        imu._mag.cal = (20.915039062, 11.880468750, 23.293359375)
        imu.gyro_filter_range = 4
        imu.accel_filter_range = 4
        print(imu.mag.cal)
        print(imu.accel.cal)
        print(imu.gyro.cal)
        mpu_addr = "MPU9250 id: {:X}".format(imu.mpu_addr)
        cmd.send_uart(mpu_addr, True)
        fuse = Fusion()
    except:
        cmd.send_uart("No imu detected", True)

    sensors.ina_init(i2c)


