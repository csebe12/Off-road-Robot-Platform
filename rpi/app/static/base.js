$(function(){
	// Connect to the socket server
	var socket = io.connect('http://' + document.domain + ':' + location.port + '/signals');
	console.log("Socket connected");


// Joystick
	var joy = new JoyStick('joyDiv');
	var x = $("#X");
	var y = $("#Y");
	x.val(0);
	y.val(0);
	var x_prev = joy.GetX();
	var y_prev = joy.GetY();
	var val_changed = false;

	// Center the joystick
	$("#joyDiv").css("text-align", "center");

	// Only send motor commands and update values when the joystick is being moved
	// Updated every 50 ms
	setInterval(function(){
		var x_current = joy.GetX();
		var y_current = joy.GetY();
		if (x_current != x_prev){
			x.val(x_current);
			val_changed = true;
		}
		if (y_current != y_prev){
			y.val(y_current);
			val_changed = true;
		}

		if (val_changed){	
			msg = "/set_speed?x=" + x_current + "&y=" + y_current;
			xhttp_send(msg);
		}
		x_prev = x_current;
		y_prev = y_current;
		val_changed = false;
	}, 50);

	var pwr = $("#pwr_ratio");
	pwr.on('input', function(){
		msg = "/pwr_ratio?mode=" + pwr.val();
		xhttp_send(msg);
	});

	var stop = $("#stop")
	stop.on('click', function() {
		msg = "/stop";
		xhttp_send(msg);
	});
// End of Joystick

	var list = $('.command_history');
	socket.on('new_msg', function(msg){
		try{
			var obj = JSON.parse(msg[1]);
			switch (obj["type"]){
				case 'gps':
					gps_data(obj);
					break;
				case 'battery':
					battery(obj);
					break;
				case 'motor_current':
					motor_current(obj);
					break;
				default:
					console.log("JSON type is not valid");
					console.log(obj);
					break;
			}
		}
		catch(err){
			list.append("<li class='" + msg[0] + "'>" + msg[1] + "</li>");
		}
	});

	var ping_dot = $('#ping');
	socket.on('ping', function(msg){
		if (msg){
			ping_dot.removeClass("inactive").addClass("active");
		}
		else {
			ping_dot.removeClass("active").addClass("inactive");
		}
	});

	// Command history will always be scrolled to the bottom
	// source: https://stackoverflow.com/questions/18614301/keep-overflow-div-scrolled-to-bottom-unless-user-scrolls-up/18614561
	// reformatted it to jQuery
	setInterval(function(){
		var atBottom = list.prop('scrollHeight') - list.prop('clientHeight') <= list.prop('scrollTop') + 1;
		if (!atBottom){
			list.scrollTop(list.prop('scrollHeight') - list.prop('clientHeight'));
		}

	}, 3000);
	
	$("#cmd_submit").on('click', function(){
		event.preventDefault();
		var cmd = $("input[name='cmd']").val();
		msg = "/command?cmd=" + cmd;
		xhttp_send(msg);
	});


	var uart_on = $("#uart_on");
	var calib = $("#calibrate");
	var rpi_re = $("#rpi_restart");
	var rpi_sh = $("#rpi_shutdown");
	var pyb_re = $("#pyb_restart");

	uart_on.on('click', function(){
		msg = "/restarts?mode=4";
		xhttp_send(msg);
	});

	calib.on('click', function(){
		msg = "/restarts?mode=3";
		xhttp_send(msg);
	});

	rpi_re.on('click', function(){
		msg = "/restarts?mode=0";
		xhttp_send(msg);
	});

	rpi_sh.on('click', function(){
		msg = "/restarts?mode=1";
		xhttp_send(msg);
	});

	pyb_re.on('click', function(){
		msg = "/restarts?mode=2";
		xhttp_send(msg);
	});

	$("#servo_submit").on('click', function(){
		var new_servo = create_servo($("#servo_setup").val());
		if (new_servo){
			msg = "/servo?func=init&num=" + $("#servo_setup").val();
			xhttp_send(msg);
		}
	});

	// Navigation buttons
	$("#start_nav").on('click', function(){
		msg = "/nav?func=start";
		xhttp_send(msg);
	});

	$("#pause_nav").on('click', function(){
		msg = "/nav?func=pause";
		xhttp_send(msg);
	});

	$("#stop_nav").on('click', function(){
		$("#next_dist").empty();
		$("#tar_head").empty();
		$("#way_num").empty();
		$("#next_coor").empty();
		msg = "/nav?func=stop";
		xhttp_send(msg);
	});

	$("#home").on('click', function(){
		msg = "/nav?func=home";
		xhttp_send(msg);
	});

	// Map user interface functions
	$("#show_waypoint").on('click', function(){
		var lat = parseFloat($("#lat").val());
		var lon = parseFloat($("#lon").val());
		if (lat !== lat){
			$("#lat")[0].setCustomValidity("Please enter the coordinate in decimal format");
		}
		else if (lon !== lon){
			$("#lon")[0].setCustomValidity("Please enter the coordinate in decimal format");
		}
		else{
			$("#lat")[0].setCustomValidity("");
			$("#lat")[0].setCustomValidity("");
			show_waypoint([lat, lon]);
		}

	});

	$("#clear_map").on('click', function(){
		gps_logger("clear");
	});

	$("#insert_waypoint").on('click', function(){
		var lat = parseFloat($("#lat").val());
		var lon = parseFloat($("#lon").val());
		var index = parseInt($("#waypoint_list").children("option:selected").val()) + 1;
		insert_waypoint(index, [lat, lon]);
	});

	$("#delete_waypoint").on('click', function(){
		var index = parseInt($("#waypoint_list").children("option:selected").val());
		delete_waypoint(index);
	});


	$("#upload_waypoint").on('click', async function(){
		var waypoints = get_waypoints();
		var waypoint_cmds = waypoints.map(x => "/command?cmd=planner/coord:"+x);
		waypoint_cmds.unshift("/command?cmd=planner/add_start");
		waypoint_cmds.push("/command?cmd=planner/add_end")
		for (var i=0;i<waypoint_cmds.length;i++){
			await sleep(150);
			xhttp_send(waypoint_cmds[i]);
		}
	});


	$("#add_home").on('click', function(){
		var lat = parseFloat($("#lat").val());
		var lon = parseFloat($("#lon").val());
		insert_waypoint(0, [lat, lon]);
	});
});


function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function xhttp_send(msg){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {}};
	xhttp.open("GET", msg, true);
	xhttp.send()
}

function gps_data(data){
	switch (data["func"]){
		case "planner":
			var tar_head = parseFloat(data["tar_head"]).toFixed(2);
			var way_dist = parseFloat(data["way_dist"]).toFixed(2);
			var way_num = parseFloat(data["way_num"]);
			var next_way_lat = parseFloat(data["next_way_lat"]).toFixed(4);
			var next_way_lon = parseFloat(data["next_way_lon"]).toFixed(4);

			$("#tar_head").text(tar_head + "°");
			$("#next_dist").text(way_dist +  " m");
			$("#way_num").text(way_num);
			$("#next_coor").text(next_way_lat + ", " + next_way_lon);

			var nav_btn = $(".nav_btn");
			switch (data["stat"]){
				case "Stop":
					nav_btn.removeClass().addClass("nav_btn");
					break;
				case "Start":
					if (nav_btn.hasClass("nav_start") == false){
						nav_btn.removeClass().addClass("nav_btn nav_start");
					}
					break;
				case "Pause":
					if (nav_btn.hasClass("nav_pause") == false){
						nav_btn.removeClass().addClass("nav_btn nav_pause");
					}
					break;
				default:
					nav_btn.removeClass().addClass("nav_btn");
					break;
			}
			break;
		case "position":
			var lat = parseFloat(data["lat"]);
			var lon = parseFloat(data["long"]);
			var hdop = parseFloat(data["hdop"]);
			var gps_dot = $("#gps_lock");
			var speed = parseFloat(data["speed"]).toFixed(2);
			$("#speed").text(speed+" m/s");
			
			// Acceptable accuracy
			if (hdop < 10){
				gps_logger("hdop", true);
				try{
					gps_logger("breadcrumb", [lat, lon]);
				}
				catch(err){}

				if (hdop < 2){
					gps_dot.removeClass().addClass("dot perfect_lock");
					gps_dot.text(hdop.toFixed(2));
				}
				else if (hdop < 5){
					gps_dot.removeClass().addClass("dot good_lock");
					gps_dot.text(hdop.toFixed(2));
				}
				else{
					gps_dot.removeClass().addClass("dot medium_lock");
					gps_dot.text(hdop.toFixed(2));
				}
			}
			else{
				gps_dot.removeClass().addClass("dot no_lock");
				gps_dot.empty();
				gps_logger("hdop", false);
			}
			$("#cur_coor").text(lat.toFixed(4) + ", "  + lon.toFixed(4));
			break;
		case "waypoints":
			var wps = data["waypoints"];
			gps_logger("waypoints", wps);
			break;
		case "next_waypoint":
			gps_logger("next_waypoint", data["index"]);
			break;
		case "heading":
			var head = parseFloat(data["head"]).toFixed(2);
			$("#cur_head").text(head + "°");
			break;
		default:
			console.log("Invalid func in gps_data():\n" + data);
			break;
	}

	// var coord1 = [50.936727, -1.383480];
	// var coord2 = [50.929087, -1.394422];
	// var coord3 = [50.928946, -1.408915];
}

function battery(data){
	var cell_1 = parseFloat(data["1"]);
	var cell_2 = parseFloat(data["2"]);
	var cell_3 = parseFloat(data["3"]);
	var cell_4 = parseFloat(data["4"]);

	if (cell_1 < 3.2){
		$("#cell_1").addClass("bat_crit");
	}
	else{
		$("#cell_1").removeClass("bat_crit");
	}
	if (cell_2 < 3.2){
		$("#cell_2").addClass("bat_crit");
	}
	else{
		$("#cell_2").removeClass("bat_crit");
	}
	if (cell_3 < 3.2){
		$("#cell_3").addClass("bat_crit");
	}
	else{
		$("#cell_3").removeClass("bat_crit");
	}
	if (cell_4 < 3.2){
		$("#cell_4").addClass("bat_crit");
	}
	else{
		$("#cell_4").removeClass("bat_crit");
	}

	$("#cell_1").text("1: " + cell_1.toFixed(1) + " V");
	$("#cell_2").text("2: " + cell_2.toFixed(1) + " V");
	$("#cell_3").text("3: " + cell_3.toFixed(1) + " V");
	$("#cell_4").text("4: " + cell_4.toFixed(1) + " V");
}

function create_servo(num){
	var check = $("#servo" + num + "_container").length;
	// First servo instance
	if (check == 0){
		$("#servo_submit").parent().after('<div class="servo_controller" id="servo' + num + '_container">' + '\n<span class="servo_label">S ' + num + '</span>' + '\n<button class="servo_dir" id="servo' + num + '_left"><</button>' + '\n<button class="servo_dir" id="servo' + num + '_right">></button>' + '\n<button id="servo' + num + '_deinit">Off</button>' + '\n</div');
		$("#servo" + num + "_deinit").on('click', {num: num}, deinit_servo);
		$("#servo" + num + "_left").on('click', {num: num, dir: "left"}, move_servo);
		$("#servo" + num + "_right").on('click', {num: num, dir: "right"}, move_servo);

		return true;
	}
	else{
		return false;
	}
}

function deinit_servo(event){
	$("#servo" + event.data.num + "_container").remove();
	msg = "/servo?func=deinit&num=" + event.data.num;
	xhttp_send(msg);
}

function move_servo(event){
	msg = "/servo?func=move&num=" + event.data.num + "&dir=" + event.data.dir
	xhttp_send(msg);
}

function motor_current(data){
	$("#motor_current").text((parseFloat(data["current"])).toFixed(1) + " mA");
}