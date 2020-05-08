var position_icon = L.icon({
    iconUrl: 'static/images/icons8-marker-32.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [16, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var no_gps_icon = L.icon({
    iconUrl: 'static/images/icons8-marker-off-32.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [16, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var home_icon = L.icon({
    iconUrl: 'static/images/icons8-home-32.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [16, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var home_icon_red = L.icon({
    iconUrl: 'static/images/icons8-home-32-red.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [16, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var waypoint_icon = L.icon({
    iconUrl: 'static/images/icons8-empty-flag-32.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [8, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var next_waypoint_icon = L.icon({
    iconUrl: 'static/images/icons8-empty-flag-32-red.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [8, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var user_waypoint_icon = L.icon({
    iconUrl: 'static/images/icons8-empty-flag-32-blue.png',

    iconSize:     [32, 32], // size of the icon
    iconAnchor:   [16, 32], // point of the icon which will correspond to marker's location
    popupAnchor:  [2, -40] // point from which the popup should open relative to the iconAnchor
});

var map = L.map('map_div', {
    center: [50.935645, -1.385669],
    zoom: 13
});

map.on('click', clicked_coordinate);

L.tileLayer( 'static/mapTiles/OSM/{z}_{x}_{y}.png', {
    minZoom: 7,
    maxZoom: 17,
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo( map );

var gps_history = [];
var gps_line;
var waypoint_line;
var last_point;
var gps_lock = false;
var waypoints = [];
var waypoint_markers = [];
var prev_next_waypoint;
var user_marker;

function gps_logger(func, data){
    switch(func){
        case "breadcrumb":
            gps_history.push(data);
            draw_history();
            break;
        case "hdop":
            gps_lock = data;
            break;
        case "waypoints":
            waypoints = data;
            waypoints_selector();
            draw_waypoints();
            break;
        case "next_waypoint":
            draw_waypoints(next_waypoint=parseInt(data)-1);
            prev_next_waypoint = parseInt(data)-1;
            break;
        case "clear":
            clear_map();
            break;
        default:
            console.log("invalid func in gps_logger(): " + func);
            break;
    }
}
// Displays the gps history of the robot
function draw_history(){
    try{
        map.removeLayer(last_point);
        map.removeLayer(gps_line);
    }
    catch(err){}
    gps_line = L.polyline(gps_history).addTo(map);
    if (gps_lock){
        last_point = L.marker(gps_history[gps_history.length - 1], {icon: position_icon}).addTo(map);
    }
    else{
        last_point = L.marker(gps_history[gps_history.length - 1], {icon: no_gps_icon}).addTo(map);
    }
    
    // 6 decimal places gives 0.111 m error
    last_point.bindPopup("Lat: " + gps_history[gps_history.length - 1][0].toFixed(6) + "<br>Lon: " + gps_history[gps_history.length - 1][1].toFixed(6));
}
// Displays waypoints on map. Updates the next waypoint icon when data is received. It also used to update the map when the user adds a new waypoint
function draw_waypoints(next_waypoint=0){
    try{
        for (var i=0;i<waypoint_markers.length;i++){
            map.removeLayer(waypoint_markers[i]);
        }
        waypoint_markers = [];
        map.removeLayer(waypoint_line);
    }
    catch(err){}
    // Only updates waypoint drawing when the next waypoint changes
    if (next_waypoint != prev_next_waypoint){
        var curr_icon;
        for (var i=0; i<waypoints.length;i++){
            if (i == next_waypoint){
                if (i == 0){
                    curr_icon = home_icon_red;
                }
                else{
                   curr_icon = next_waypoint_icon; 
                }
            }
            else{
                curr_icon = waypoint_icon;
                if (i == 0){
                    curr_icon = home_icon;
                }
            }
            waypoint_markers.push(new L.marker(waypoints[i], {icon: curr_icon}).bindPopup("#: " + (i+1) + "<br>Lat: " + waypoints[i][0].toFixed(6) + "<br>Lat: " + waypoints[i][1].toFixed(6)).addTo(map));
        }
        waypoint_line = L.polyline(waypoints, {color: 'orange'}).addTo(map);
    }
}

function clicked_coordinate(e){
    var lat_c, lon_c;
    lat_c = e.latlng.lat;
    lon_c = e.latlng.lng;
    $("#lat").val(lat_c.toFixed(6));
    $("#lon").val(lon_c.toFixed(6));
    show_waypoint([lat_c, lon_c]);
}

function show_waypoint(data){
    try{
        map.removeLayer(user_marker);
    }
    catch(err){}
    user_marker = L.marker(data, {icon: user_waypoint_icon}).bindPopup("Lat: " + data[0].toFixed(6) + "<br>Lon: " + data[1].toFixed(6)).addTo(map);
}

function waypoints_selector(){
    $("#waypoint_list").empty();
    for (var i=0;i<waypoints.length;i++){
        $("#waypoint_list").append('<option value=' + i + ' class="waypoints_option"><strong>#' + (i+1) + ': </strong>' + 'Lat: ' + waypoints[i][0].toFixed(6) + ' Lon: ' + waypoints[i][1].toFixed(6));
    }
    $("#waypoint_list").val(waypoints.length-1);
}

function insert_waypoint(index, data){
    waypoints.splice(index, 0, data);
    map.removeLayer(user_marker);
    waypoints_selector();
    draw_waypoints();
}

function delete_waypoint(index){
    waypoints.splice(index, 1);
    waypoints_selector();
    draw_waypoints();
}

function get_waypoints(){
    return waypoints;
}

function clear_map(){
    try{
        map.removeLayer(gps_line);       
    }
    catch(err){}
    try{
        map.removeLayer(user_marker);
    }
    catch(err){}
    try{
        map.removeLayer(waypoint_line);
        for (var i=0; i<waypoint_markers.length;i++){
            map.removeLayer(waypoint_markers[i]);
        }   
    }
    catch(err){}

    waypoints = [];
    gps_history = [];
    $("#waypoint_list").empty();
}