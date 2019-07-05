#!/usr/bin/python3

import servoLib
import math, time

def main():
    near = servoLib.Servo(18)
    far = servoLib.Servo(17)

    for i in range(500):
        near.setPosition(0.8 * math.sin(0.04 * i))
        far.setPosition(-0.8 * math.sin(0.04 * i))
        time.sleep(0.02)


if __name__ == "__main__":
    main()
