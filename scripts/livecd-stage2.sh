#!/bin/bash

set -ex

# Permit root logins without a password on local shells
sed -i '/^root:/s/:\*:/::/' /etc/shadow
echo ttyS0 >> /etc/securetty

# Autoconfigure network from DHCP
cat << NETWORK > /etc/systemd/network/wired.network
[Match]
Type=ether

[Network]
DHCP=both
NETWORK

cat << NETWORK > /etc/systemd/network/wireless.network
[Match]
Type=wlan

[Network]
DHCP=both
NETWORK

systemctl enable systemd-networkd systemd-resolved

exit 0
