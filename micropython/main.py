import _thread
import global_variables
import cmd
import sensors
from utime import ticks_ms, ticks_diff, sleep_ms
import gc

def main():
    global_variables.init()
    print('Board initialised')
    # _thread.start_new_thread(sensors.fusion_read, ())
    _thread.start_new_thread(global_variables.pid_test.start_pid, ())

    i = 0
    while True:
        if global_variables.uart.any() > 0:
            cmd.command()
        elif global_variables.uart_gps.any() > 0:
            global_variables.gps_device.update()
        i += 1
        if i % 100 == 0:
            gc.collect()


        # if i % 20 == 0:
        #     gc.collect()
        # i += 1
        # if i % 5 == 0:
        #     print("Heading, Pitch, Roll: {:7.3f} {:7.3f} {:7.3f}".format(global_variables.fuse.heading, global_variables.fuse.pitch, global_variables.fuse.roll))
        # sleep_ms(20)
        # i += 1


if __name__ == '__main__':
    main()