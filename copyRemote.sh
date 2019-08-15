#!/bin/bash

ADDR=pi@192.168.43.26
DIR=/home/pi/src/python/RoboticArm/
PROGRAM=./control.py
echo "Copying this directory to $ADDR:$DIR and launching $PROGRAM remotely"

scp * $ADDR:$DIR
