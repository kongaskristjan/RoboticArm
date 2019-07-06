#!/usr/bin/python3

import arm

def main():
    lineDrawer = arm.Arm()
    lineDrawer.drawText("abba", 8, 20, 0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
