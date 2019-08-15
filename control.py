#!/usr/bin/python3

import arm, time, fire

def main(speed=1):
    speedActive = 5 * speed
    speedInactive = 16 * speed
    letterSleep = 0.5 / speed

    lineDrawer = arm.Arm()
    #lineDrawer.setStraight()
    #time.sleep(5)
    #lineDrawer.drawText("ABCDEFGHIJKLMNOPQRSTUVWXYZ", speedActive, speedInactive, letterSleep)
    #lineDrawer.drawText("., !?", speedActive, speedInactive, letterSleep)
    lineDrawer.drawText("Tere Liisi, Madli, Kristjan, Lauri, Rutt, Olav ja kassid!", speedActive, speedInactive, letterSleep)

if __name__ == "__main__":
    try:
        fire.Fire(main)
    except KeyboardInterrupt:
        del arm
