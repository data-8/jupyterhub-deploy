#!/bin/bash

# Get kernel major/minor/micro
k=$(uname -r | sed -e 's/-.*//')

# Create name of latest kernel image extra package
p=$(dpkg --get-selections | grep linux-image-${k} | sort | tail -1 | awk '{print $1}' | sed -e 's/image/image-extra/')

# Install the linux-image-extra-${k}-... package
apt-get install $p
