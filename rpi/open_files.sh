#!/bin/sh
cd /home/pi/Desktop
rsub board_restarts.py
rsub comms.py
rsub thread.py
cd app
rsub global_vars.py
rsub web_server.py
cd templates
rsub base.html
cd ../static
rsub map.js
rsub base.js
rsub styles/styling.css
