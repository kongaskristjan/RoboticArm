#!/usr/bin/python3

import arm, time, fire

def main(speed=1, text="Hello world!", test=False):
    speedActive = 5 * speed
    speedInactive = 16 * speed
    letterSleep = 0.5 / speed

    lineDrawer = arm.Arm()
    if test:
        lineDrawer.setStraight()
        time.sleep(2)
    else:
        lineDrawer.drawText(str(text), speedActive, speedInactive, letterSleep)


if __name__ == "__main__":
    try:
        fire.Fire(main)
    except KeyboardInterrupt:
        del arm
