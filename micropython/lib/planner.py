import cmd
import math
import global_variables
import _thread
import ujson

log_flag = False
debug_flag = False


class PLANNER:
    def __init__(self, gps):
        self._gps = gps
        self._home = (None, None)               # tuple: lat, long (float)
        self._waypoints = [(None, None)]
                                                # Converts the input into float. Must be two iterable objects
                                                # in the form of lat, lon
                                                # Input values can be float or string
        self._next_waypoint = (None, None)      # tuple: lat, long
        self._waypoints_num = None
        self._curr_waypoint_num = 0
        self._current_pos = (None, None)        # tuple: lat, long
        self._distance = None
        self._bearing = None                    # degrees
        self._planner_init = False              # Tracks if waypoints have been initialised
        self.status = "Stop"
        self._add = False                       # If true, coordinates are added to the waypoints
        self.i = 0

    # Returns a flag which is true if the calculation proceeded and a tuple (distance, bearing)
    # If there was an error, false, (None, None) is returned
    def dist_bearing(self):
        if ((self._gps.pos_fix > 0) or (self._gps.status == "A")) and self._gps.latitude is not None:
            self._current_pos = (float(self._gps.latitude), float(self._gps.longitude))
            try:
                # A is current_pos in rad, B is next_waypoint in rad
                A = ([0.0174533*x for x in self._current_pos])
                B = ([0.0174533*x for x in self._next_waypoint])
                d_long = float(B[1] - A[1])
                # This is true North heading
                self._bearing = math.atan2((math.sin(d_long)*math.cos(B[0])), (math.cos(A[0])*math.sin(B[0])-math.sin(A[0])*math.cos(B[0])*math.cos(d_long)))*57.29577951
                if self._bearing > 180:
                    self._bearing -= 360
                # Distance calculated using the haversine formula
                # Earth's mean radius in m
                R = 6371000
                d_lat = float(B[0] - A[0])
                a = math.sin(d_lat/2)**2 + math.cos(A[0])*math.cos(B[0])*math.sin(d_long/2)**2
                c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
                self._distance = R*c
                # Updates waypoints if robot has reached waypoint
                self.waypoint_manager()
                self.i = 0
                return True, (self._distance, self._bearing)
            except TypeError:
                if self.i > 5:
                    cmd.send_uart("Inaccurate hdop in dist_bearing", log_flag)
                    self.pause_planner()
                self.i += 1
                return False, (None, None)
        else:
            if self.i > 5:
                cmd.send_uart("Inaccurate pos in dist_bearing", log_flag)
                self.pause_planner()
            self.i += 1
            return False, (None, None)

    def waypoint_manager(self):
        if self._distance < 2:
            if self._curr_waypoint_num < self._waypoints_num:
                try:
                    self._curr_waypoint_num += 1
                    self._next_waypoint = self._waypoints[self._curr_waypoint_num]
                    msg = "Waypoint reached, heading to #{0} at {1}\n".format(str(self._curr_waypoint_num+1), str(self._next_waypoint))
                    cmd.send_uart(msg, log_flag)
                    msg = {"type": "gps", "func": "curr_waypoint", "index": self._curr_waypoint_num+1}
                    msg = ujson.dump(msg)
                    cmd.send_uart(msg, log_flag)
                except IndexError:
                    cmd.send_uart("Waypoint manager IndexError\n", log_flag)

            else:
                cmd.send_uart("All waypoints have been covered", log_flag)
                self.stop_planner()
                msg = {"type": "gps", "func": "next_waypoint", "index": -1}
                msg = ujson.dump(msg)
                cmd.send_uart(msg, log_flag)

    def waypoint_init(self):
        try:
            self._waypoints_num = len(self._waypoints) - 1
            self._home = self._waypoints[0]
            self._curr_waypoint_num = 0
            self._next_waypoint = self._waypoints[0]
            cmd.send_uart("{0:d} waypoints initialised\n".format(len(self._waypoints)), log_flag)
            msg = {"type": "gps", "func": "waypoints", "waypoints": self._waypoints}
            msg = ujson.dumps(msg)
            cmd.send_uart(msg, log_flag)
            if debug_flag is True:
                cmd.debug(msg, debug_flag)
            return True
        except (TypeError, IndexError):
            cmd.send_uart("No waypoints", log_flag)
            return False

    def waypoint_coord(self, waypoint):
        if self._add is True:
            try:
                self._waypoints.append((float(waypoint[0]), float(waypoint[1])))
            except ValueError:
                cmd.send_uart("Invalid coordinate format", log_flag)
                print(waypoint[0], waypoint[1])

    def waypoint_add(self, start):
        if start is True:
            self._waypoints.clear()
        else:
            cmd.send_uart("{0:d} waypoints added\n".format(len(self._waypoints)), log_flag)
        self._add = start

    def planner_data(self):
        msg = {"type": "gps", "func": "planner", "stat": str(self.status), "tar_head": str(self._bearing),
               "way_num": str(self._curr_waypoint_num+1), "next_way_lat": str(self._next_waypoint[0]),
               "next_way_lon": str(self._next_waypoint[1]), "way_dist": str(self._distance)}
        msg = ujson.dumps(msg)

        cmd.send_uart(msg, log_flag)
        if debug_flag is True:
            cmd.debug(msg, debug_flag)

    def start_planner(self):
        try:
            if ((self._gps.pos_fix > 0) or (self._gps.status == "A")) and self._gps.latitude is not None:
                if self._planner_init is False:
                    if self.waypoint_init() is True:
                        self.status = "Start"
                        global_variables.pid_test.start_update()
                        cmd.send_uart("Autonomous mode started\n", log_flag)
                        self._planner_init = True
                    else:
                        cmd.send_uart("Couldn't initialise waypoints\n", log_flag)
                else:
                    self.status = "Start"
                    self.resume_planner()
            else:
                cmd.send_uart("GPS accuracy not good enough\n", log_flag)
        except TypeError:
            cmd.send_uart("No GPS signal\n", log_flag)

    # This deinitialises the timers in the pid library and disables the pid() method to update itself
    def pause_planner(self):
        if self._planner_init is True:
            self.status = "Pause"
            global_variables.pid_test.stop_update()
            cmd.send_uart("Autonomous mode paused\n", log_flag)
        else:
            cmd.send_uart("Autonomous mode hasn't been started yet\n", log_flag)

    def stop_planner(self):
        self.status = "Stop"
        global_variables.pid_test.stop_update()
        self._distance = None
        self._curr_waypoint_num = 0
        self._waypoints.clear()
        self._next_waypoint = (None, None)
        self._bearing = None
        self._planner_init = False
        cmd.send_uart("Autonomous mode stopped\n", log_flag)

    def resume_planner(self):
        if self._planner_init is True:
            global_variables.pid_test.start_update()
            cmd.send_uart("Autonomous mode resumed\n", log_flag)
        else:
            cmd.send_uart("Autonomous mode hasn't been started yet\n", log_flag)

    def go_home(self):
        if self._planner_init is True:
            self.status = "Start"
            self._waypoints = [self._home]
            self._next_waypoint = self._home
            self._waypoints_num = 1
            self._curr_waypoint_num = 1
            self.resume_planner()
            msg = {"type": "gps", "func": "waypoints", "waypoints": self._waypoints}
            msg = ujson.dumps(msg)
            cmd.send_uart(msg, log_flag)
            if debug_flag is True:
                cmd.debug(msg, debug_flag)
        else:
            cmd.send_uart("Autonomous mode hasn't been started yet\n", log_flag)