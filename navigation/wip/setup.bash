#!/usr/bin/env bash

# This script will secure copy the appropriate files to host machine and run prerequisite commands
# NOTE: You must be in the baxter-demo/navigation directory

USER=mb
HOST=NUC.local   # or use IP address in cmd line arg if need to distinguish btw Alice and Bob
PATH_TO_PRIVATE_KEY=./baxter_mb_ssh_key
DEMO_SCRIPT=navigation.py

if [ ! -z "$1" ]; then HOST=$1; fi

# SCP current demo script to mobility base
scp -i $PATH_TO_PRIVATE_KEY -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $DEMO_SCRIPT $USER@$HOST:~/

ssh -i $PATH_TO_PRIVATE_KEY -tt -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null $USER@$HOST /bin/bash <<-"ENDSSH"
    bash mobility_base_config.bash
    roslaunch mobility_base_bringup mobility_base.launch &
    sleep 3
    rostopic pub -r 10 /mobility_base/suppress_wireless std_msgs/Empty &
ENDSSH