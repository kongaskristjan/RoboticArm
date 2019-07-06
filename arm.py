
import devices, letters
import math, time

class Arm:
    def __init__(self):
        self.x, self.y = None, None
        self.near = devices.Servo(18, offsetAngle=0.12)
        self.far = devices.Servo(17, offsetAngle=1.08)
        self.led = devices.Led(27)

    def drawText(self, text, speedActive, speedInactive, letterSleep):
        for chr in text:
            coords = letters.coordsMap[chr.upper()]
            self.drawSegments(coords, speedActive, speedInactive)
            self.led.setValue(False)
            time.sleep(letterSleep)

    def drawSegments(self, coords, speedActive, speedInactive):
        for innerCoords in coords:
            x, y = innerCoords[0]
            self.draw(x, y, speedInactive, False)
            for x, y in innerCoords[1:]:
                self.draw(x, y, speedActive, True)

    def draw(self, x, y, speed, ledValue):
        self.led.setValue(ledValue)
        if self.x is None and self.y is None:
            self.x, self.y = x, y
            self.moveToPosition(x, y, 0)
            return

        dt = 0.01
        dx = speed * dt * (x - self.x) / (math.hypot(x - self.x, y - self.y) + 1e-6)
        dy = speed * dt * (y - self.y) / (math.hypot(x - self.x, y - self.y) + 1e-6)
        for i in range(int(math.hypot(x - self.x, y - self.y) / (speed * dt))):
            self.moveToPosition(self.x + i * dx, self.y + i * dy, dt)
        self.x, self.y = x, y

    def moveToPosition(self, x, y, t):
        nearAngle, farAngle = self.computeAngles(x, y)
        self.near.setPosition(-nearAngle)
        self.far.setPosition(-farAngle)
        time.sleep(t)

    def computeAngles(self, x, y):
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
