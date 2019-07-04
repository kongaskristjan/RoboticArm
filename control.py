#!/usr/bin/python3

import servoLib
import math, time

def main():
    near = servoLib.Servo(15)
    far = servoLib.Servo(14)

    while True:
        near.setPosition(math.pi / 2)
        time.sleep(1)
        near.setPosition(-math.pi / 2)
        time.sleep(1)


if __name__ == "__main__":
    main()
