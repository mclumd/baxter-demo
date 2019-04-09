#!/bin/bash

if [ -z "$1" ]; then
    echo " >>> Navigation will use commands from terminal"
    ./client.py
elif [ "$1" == "voice-control" ]; then
    if [ "$(which pocketsphinx_continuous > /dev/null; echo $?)" != 0 ]; then
        echo "Error: Pocketsphinx_continuous is not installed; aborting" && exit 1
    fi
    echo " >>> Navigation will use voice commands from microphone; check server output for commands heard"
    pocketsphinx_continuous -inmic yes 2> /dev/null | ./client.py
else
    echo " >>> Usage: ./start.sh [voice-control]"
fi
