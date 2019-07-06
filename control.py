#!/usr/bin/python3

import devices
import math, time, random

near = devices.Servo(18, offsetAngle=0.12)
far = devices.Servo(17, offsetAngle=1.08)
led = devices.Led(27)

def computeAngles(x, y):
    l0, l1 = 5.5, 7.6
    dist = math.hypot(x, y)

    # Compute result according to transformation (x, y) -> (dist, 0)
    S = 0.5 * (l0 + l1 + dist)
    A = math.sqrt(S * (S - l0) * (S - l1) * (S - dist))
    h = 2. * A / dist
    angle0 = math.asin(h / l0)
    angle1Opposite = math.asin(h / l1)
    angle1 = angle0 + angle1Opposite

    # Transform (dist, 0) -> (x, y)
    angle0 += math.atan2(y, x)
    return angle0, angle1


def moveToPosition(x, y, t):
    nearAngle, farAngle = computeAngles(x, y)
    near.setPosition(-nearAngle)
    far.setPosition(-farAngle)
    time.sleep(t)


class LineDrawer:
    def __init__(self):
        self.x, self.y = None, None

    def draw(self, x, y, speed):
        if self.x is None and self.y is None:
            self.x, self.y = x, y
            moveToPosition(x, y, 0)
            return

        dt = 0.01
        dx = speed * dt * (x - self.x) / (math.hypot(x - self.x, y - self.y) + 1e-6)
        dy = speed * dt * (y - self.y) / (math.hypot(x - self.x, y - self.y) + 1e-6)
        for i in range(int(math.hypot(x - self.x, y - self.y) / (speed * dt))):
            moveToPosition(self.x + i * dx, self.y + i * dy, dt)
        self.x, self.y = x, y


def main():
    lineDrawer = LineDrawer()
    r = 3.5
    speed = 8

    for i in range(11):
        angle = (2 / 5) * (2 * math.pi) * i
        led.setValue(random.randint(0, 1))
        lineDrawer.draw(13 - r + r * math.cos(angle), r * math.sin(angle), speed)
    time.sleep(0.4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    del near, far, led
