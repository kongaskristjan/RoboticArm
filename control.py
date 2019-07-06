#!/usr/bin/python3

import arm

def main():
    speedActive = 5
    speedInactive = 16
    letterSleep = 0.5

    lineDrawer = arm.Arm()
    #lineDrawer.drawText("ABCDEFGHIJKLMNOPQRSTUVWXYZ", speedActive, speedInactive, letterSleep)
    #lineDrawer.drawText("., !?", speedActive, speedInactive, letterSleep)
    lineDrawer.drawText("Tere Liisi, Madli, Kristjan, Lauri, Rutt, Olav ja kassid!", speedActive, speedInactive, letterSleep)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
