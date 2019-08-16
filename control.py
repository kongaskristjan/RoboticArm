#!/usr/bin/python3

import arm, coordinateTransform
import time, fire, math

def main(speed=1, text="Hello world!", test=False, brightness=0.05, angle=0):
    speedActive = 5 * speed
    speedInactive = 16 * speed
    letterSleep = 0.5 / speed

    tfm = coordinateTransform.CoordinateTransform(9.7, angle=math.pi*angle/180)
    lineDrawer = arm.Arm(tfm, speedActive, speedInactive, letterSleep, brightness)
    if test:
        lineDrawer.setStraight()
        time.sleep(2)
    else:
        lineDrawer.drawText(str(text))


if __name__ == "__main__":
    try:
        fire.Fire(main)
    except KeyboardInterrupt:
        del arm
