from pyb import Timer
import motor
import cmd
import ujson
import sensors
import global_variables
from utime import sleep_ms, ticks_us, ticks_diff

log_flag = False
debug_flag = False


class PID:
    def __init__(self, P, I, D, target_fn, target_freq):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.target = 0                             # Degrees, planner.dist_bearing(), returns flag, (dist, bear)
        self.feedback = 0                           # Degrees
        self.error = 0                              # Degrees
        self.pid_out = 0
        self.output = (0, 0)                        # (left_pwr, right_pwr)
        self.prev_error = 0
        self.error_sum = 0
        self.base_speed = 0
        self.t_fn = target_fn
        self.target_flag = False                    # Set to true by the timer interrupt
        self.t_c_top = round(500/target_freq)       # Counter top values. Timer is set to 100 Hz
        self.t_c = 0                                # Target counter incremented when the timer triggers
        self.timer = None                           # Timer objects interrupting at period specified by user
        self.enable = False
        self.LIMITER = 1                            # Limits the output for testing
        self.POWER_LIMIT = 90
        self.BASE_PWR = 50
        self.log_msg = None
        self.i = 0


    def pid(self):
        # Updating the target variable
        if self.target_flag is True:
            # t_fn is planner.dist_bearing()
            flag, (dist, bear) = self.t_fn()
            self.target_flag = False
            if flag is True:
                self.target = bear
            else:
                return False

        self.feedback = global_variables.fuse.heading

        # Error term
        self.error = self.target - self.feedback
        # Always rotating in the shortest direction
        if self.error > 180:
            self.error = 360-self.error
        elif self.error < -180:
            self.error = 360+self.error
        if (self.error > -20) and (self.error < 20):
            self.error_sum += self.error
        self.pid_out = self.Kp * self.error          # Proportional
        self.pid_out += self.Kd * self.prev_error    # Derivative
        self.pid_out += self.Ki * self.error_sum     # Integral
        self.prev_error = self.error

        self.base(self.error)
        # If error is negative (left turn needed to reduce error), so is pid_out. right speed increases, left speed decreases, vice versa
        self.output = (round(((self.base_speed + self.pid_out/2) * self.LIMITER), 0), round(((self.base_speed - self.pid_out/2) * self.LIMITER), 0))
        if (abs(self.output[0]) < self.POWER_LIMIT) and (abs(self.output[1]) < self.POWER_LIMIT):
            motor.motor_abs(("l", self.output[0]), ("r", self.output[1]))
        else:
            cmd.send_uart("pid out of range\n", log_flag)
            self.error_sum = 0
        return True

    def base(self, error):
        abs_err = abs(error)
        self.base_speed = -(self.BASE_PWR/180)*abs_err + self.BASE_PWR

    def update(self, timer):
        self.t_c += 1
        if self.t_c % self.t_c_top == 0:
            self.target_flag = True

    def start_update(self):
        # 16-bit timer
        self.timer = Timer(9)
        self.timer.init(freq=100)
        self.timer.callback(self.update)
        self.enable = True
        self.error_sum = 0
        cmd.send_uart("PID timers started\n", log_flag)

    def stop_update(self):
        try:
            self.timer.deinit()
        except AttributeError:
            cmd.send_uart("PID not initialised\n", log_flag)
        self.enable = False
        self.error_sum = 0
        motor.motor_abs(("l", 0), ("r", 0))
        cmd.send_uart("PID stopped\n", log_flag)

    def start_pid(self):
        # Allows time for the first IMU reading to be completed
        sleep_ms(12)
        cmd.send_uart("PID thread started", True)
        print("PID thread started")
        self.enable = False
        i = 0
        while True:
            if i % 5 == 0:
                if self.enable:
                    self.pid()
            if i % 3 == 0:
                try:
                    acc = global_variables.imu.accel.xyz
                    gyr = global_variables.imu.gyro.xyz
                    mag = global_variables.imu.mag.xyz
                except:
                    cmd.send_uart("MPU reading error", log_flag)
            if i % 300 == 0:
                msg = {"type": "gps", "func": "heading", "head": str(global_variables.fuse.heading)}
                msg = ujson.dumps(msg)
                cmd.send_uart(msg, log_flag)
                # print(global_variables.fuse.heading)
            global_variables.fuse.update(acc, gyr, mag)
            i += 1


    def set_pid(self, P, I, D):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        if debug_flag is True:
            cmd.debug("PID set", debug_flag)

    def get_pid(self):
        return self.Kp, self.Ki, self.Kd

    def set_pwr(self, base_pwr):
        if (base_pwr >= 0) and (base_pwr <= 100):
            self.BASE_PWR = base_pwr
            return True
        else:
            return False

    def get_pwr(self):
        return self.BASE_PWR

