#!/usr/bin/python3

import Arm

def main():
    coords = [
        [
            Arm.Coords(9, -3),
            Arm.Coords(9, 3),
        ],
        [
            Arm.Coords(9, -3),
            Arm.Coords(12, -3),
        ],
        [
            Arm.Coords(9, 0),
            Arm.Coords(12, 0),
        ],
        [
            Arm.Coords(9, 3),
            Arm.Coords(12, 3),
        ],
    ]

    lineDrawer = Arm.LineDrawer()
    lineDrawer.drawSegments(coords, 8, 40) # draw an "E"

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
