#!/bin/sh
sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
cd /etc
echo "Modifying dhcpcd"
sudo cp dhcpcd-access.conf dhcpcd.conf
echo "Script will be launched on startup"
sudo cp rc-access.local rc.local
echo "Access point setup done"
