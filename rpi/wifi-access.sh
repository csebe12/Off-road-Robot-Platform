#!/bin/sh
sudo systemctl disable dnsmasq
sudo systemctl disable hostapd
cd /etc
echo "Modifying dhcpcd"
sudo cp dhcpcd-wifi.conf dhcpcd.conf
echo "Removing script to launch on startup"
sudo cp rc-wifi.local rc.local
echo "Wifi reverting done"
