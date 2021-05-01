#!/bin/bash

set -ex

# Permit root logins without a password on local shells
sed -i '/^root:/s/:\*:/::/' /etc/shadow
echo ttyS0 >> /etc/securetty

exit 0
