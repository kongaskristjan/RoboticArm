
import Adafruit_PCA9685 as pcalib
import math

freq = 60

minPulse = 500 # us
maxPulse = 2500 # us
minAngle = -math.pi / 2
maxAngle = math.pi / 2
pulseQuantization = 2**12

# Initialise the PCA9685 using the default address (0x40).
pwm = pcalib.PCA9685()
pwm.set_pwm_freq(60)

class Servo:
    def __init__(self, channel):
        self.channel = channel

    def setPosition(self, radians):
        relativePosition = (radians - minAngle) / (maxAngle - minAngle)
        assert -0.001 < relativePosition < 1.001
        pulse = minPulse + (maxPulse - minPulse) * relativePosition
        quantized = int(pulse * freq * pulseQuantization / 1e6)

        print(quantized)
        pwm.set_pwm(self.channel, 0, quantized)
        #setServoPulse(self.channel, int(pulse))
        #setServoPulse(self.channel, int(pulse))


# Helper function to make setting a servo pulse width simpler.
def setServoPulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)
