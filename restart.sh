#!/bin/bash

# Script to assist in stopping, cleaning, and relaunching zookws.
#
# For example, running the below:
# $ ./restart.sh main echo
#
# Will stop any running containers, clean the `main` and `echo` containers
# and finally relaunch all the containers.
#
# Note that running this script without any arguments amounts to a stop-and-restart.
#
# Author: amirf@mit.edu

cd /home/student/lab

# First stop any containers
./zookstop.py

# Then clean any containers which the caller specifies
for container in ${BASH_ARGV[*]}; do
    echo "Cleaning ${container}"
    ./zookclean.py $container
done

# Finally, launch the containers anew
./zookld.py
