
import pigpio
import math

minPulse = 500 # us
maxPulse = 2500 # us
minAngle = -math.pi / 2
maxAngle = math.pi / 2

pi = pigpio.pi()

class Servo:
    def __init__(self, gpio, offsetAngle=0):
        self.gpio = gpio
        self.offsetAngle = offsetAngle
        pi.set_mode(gpio, pigpio.OUTPUT)

    def setPosition(self, radians):
        relativePosition = (radians + self.offsetAngle - minAngle) / (maxAngle - minAngle)
        assert -0.001 < relativePosition < 1.001
        pulse = int(minPulse + (maxPulse - minPulse) * relativePosition)

        pi.set_servo_pulsewidth(self.gpio, pulse)

    def __del__(self):
        pi.set_mode(self.gpio, pigpio.INPUT)


class Led:
    def __init__(self, gpio, brightnessMultipler=1, frequency=500):
        self.gpio = gpio
        self.brightnessMultiplier = brightnessMultipler
        pi.set_mode(gpio, pigpio.OUTPUT)
        pi.set_PWM_frequency(self.gpio, frequency)

    def setValue(self, brightness):
        if type(brightness) == bool:
            brightness = int(brightness)

        dutycycle = int(255.5 * self.brightnessMultiplier * brightness)
        assert 0 <= dutycycle <= 255
        pi.set_PWM_dutycycle(self.gpio, dutycycle)

    def __del__(self):
        pi.write(self.gpio, 0)
        pi.set_mode(self.gpio, pigpio.INPUT)
