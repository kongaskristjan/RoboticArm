
import math

class CoordinateTransform:
    def __init__(self, deltaX, angle=0):
        self.deltaX = deltaX
        self.angle = angle

    def __call__(self, x, y):
        sn, cs = math.sin(self.angle), math.cos(self.angle)
        x, y = cs * x + sn * y, -sn * x + cs * y
        x += self.deltaX
        return x, y