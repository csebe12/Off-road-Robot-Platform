# Light-weight library to decode GPS data based on the NMEA-0183 protocol
# Library was originally written for GP-20U7
import cmd
import ujson
from utime import sleep_ms
import global_variables

log_flag = False
debug_flag = False


class GPS:
    def __init__(self, uart):
        self._uart = uart
        self.utc_time = None        # Tuple: hour, minute, second
        self.latitude = None        # Float: decimal degrees N: +, S: -
        self.longitude = None       # Float: decimal degrees E: +, W: -
        self.pos_fix = None         # 0: invalid, 1-3: valid
        self.status = "V"           # A: data valid, V: data invalid
        self.sat_used = None        # 0-12
        self.hdop = 20              # 1: ideal, 1-2: excellent, 2-5: good, 5-10: moderate, >20: poor
        self.pdop = 20
        self.vdop = 20
        self.course_t = None        # True heading, degrees
        self.course_m = None        # Magnetic heading, degrees
        self.speed = None           # m/s

    # based on source: http://doschman.blogspot.com/2013/01/calculating-nmea-sentence-checksums.html
    # Returns true if msg is valid
    def checksum(self, msg):
        cksum_start = msg.find("*")
        if cksum_start is not -1:
            cksum = msg[msg.find("*")+1:]
            # Last 2 chars + '\r\n'
            if len(cksum) == 4:
                ckdata = msg[msg.find("$")+1:msg.find("*")]
                cktest = 0
                for char in ckdata:
                    cktest ^= ord(char)
                try:
                    if hex(cktest) == hex(int(cksum, 16)):
                        return True
                    else:
                        return False
                except ValueError:
                    return False
        else:
            return False

    def print_msg(self):
        msg = self._uart.readline()
        if msg is not None:
            cmd.send_uart(msg, log_flag)

    def gps_data(self):
        try:
            msg = {"type": "gps", "func": "position", "lat": "{:.7f}".format(self.latitude), "long": "{:.7f}".format(self.longitude),
                   "hdop": str(self.hdop), "speed": "{:.2f}".format(self.speed)}
        except ValueError:
            msg = {"type": "gps", "func": "position", "lat": str(self.latitude), "long": str(self.longitude),
                   "hdop": str(self.hdop), "speed": str(self.speed)}

        msg = ujson.dumps(msg)

        cmd.send_uart(msg, log_flag)
        if debug_flag is True:
            cmd.debug(msg, debug_flag)

    # Return true if valid data has been received, otherwise false
    def update(self):
        msg = self._uart.readline()
        if msg is not None:
            try:
                data = msg.decode()
                if self.checksum(data) is True:
                    data = data.strip().split(',')
                    data_id = data[0]
                else:
                    return False
            except UnicodeError:
                return False

            if data_id == "$GPGGA":
                flag = self._gpgga(data[1:])
            elif data_id == "$GPGSA":
                flag = self._gpgsa(data[1:])
            elif data_id == "$GPVTG":
                flag = self._gpvtg(data[1:])
            elif data_id == "$GPGLL":
                flag = self._gpgll(data[1:])
            elif data_id == "$GPRMC":
                flag = self._gprmc(data[1:])
            else:
                flag = False

            if flag is True:
                return True
            else:
                return False

    # The functions below return true if all of the data has been updated, false if there were any errors
    def _gpgga(self, data):
        try:
            try:
                self.pos_fix = (int(data[5]))
            except (ValueError, IndexError):
                self.pos_fix = 0
                pass

            if self.pos_fix > 0:
                if data[2] == "N":
                    self.latitude = (int(data[1][0:2]) + float(data[1][2:9])/60)
                elif data[2] == "S":
                    self.latitude = -1*(int(data[1][0:2]) + float(data[1][2:9])/60)
                if data[4] == "E":
                    self.longitude = (int(data[3][0:3]) + float(data[3][3:9])/60)
                elif data[4] == "W":
                    self.longitude = -1*(int(data[3][0:3]) + float(data[3][3:9])/60)

            self.hdop = (float(data[7]))
            self.utc_time = (int(data[0][0:2]), int(data[0][2:4]), int(data[0][4:6]))
            self.sat_used = (int(data[6]))
            return True
        except (ValueError, IndexError):
            return False

    def _gpgsa(self, data):
        try:
            self.pdop = (float(data[14]))
            self.hdop = (float(data[15]))
            self.vdop = (float(data[16]))
            return True
        except (ValueError, IndexError):
            return False

    def _gpvtg(self, data):
        try:
            self.course_t = (float(data[0]))
            self.course_m = (float(data[2]))
            self.speed = (float(data[6]) * (5/18))
            return True
        except (ValueError, IndexError):
            return False

    def _gpgll(self, data):
        try:
            # Update coordinates if data is valid
            self.status = data[5]
            if self.status == "A":
                if data[1] == "N":
                    self.latitude = (int(data[0][0:2]) + float(data[0][2:9])/60)
                elif data[1] == "S":
                    self.latitude = -1*(int(data[0][0:2]) + float(data[0][2:9])/60)
                if data[3] == "E":
                    self.longitude = (int(data[2][0:3]) + float(data[2][3:9])/60)
                elif data[3] == "W":
                    self.longitude = -1*(int(data[2][0:3]) + float(data[2][3:9])/60)
        except (ValueError, IndexError):
            self.status = "V"
            return False

    def _gprmc(self, data):
        try:
            self.status = data[1]
            try:
                self.speed = (float(data[6]) / 1.944)
            except (ValueError, IndexError):
                pass
            if self.status == "A":
                if data[3] == "N":
                    self.latitude = (int(data[2][0:2]) + float(data[2][2:9]) / 60)
                elif data[3] == "S":
                    self.latitude = -1 * (int(data[2][0:2]) + float(data[2][2:9]) / 60)
                if data[5] == "E":
                    self.longitude = (int(data[4][0:3]) + float(data[4][3:9]) / 60)
                elif data[5] == "W":
                    self.longitude = -1 * (int(data[4][0:3]) + float(data[4][3:9]) / 60)
        except (ValueError, IndexError):
            self.status = "V"
            return False