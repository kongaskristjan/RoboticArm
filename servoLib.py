
import pigpio
import math

minPulse = 500 # us
maxPulse = 2500 # us
minAngle = -math.pi / 2
maxAngle = math.pi / 2

pi = pigpio.pi()

class Servo:
    def __init__(self, gpio):
        self.gpio = gpio
        pi.set_mode(gpio, pigpio.OUTPUT)

    def setPosition(self, radians):
        relativePosition = (radians - minAngle) / (maxAngle - minAngle)
        assert -0.001 < relativePosition < 1.001
        pulse = int(minPulse + (maxPulse - minPulse) * relativePosition)

        pi.set_servo_pulsewidth(self.gpio, pulse)

    def __del__(self):
        pi.set_mode(self.gpio, pigpio.INPUT)
