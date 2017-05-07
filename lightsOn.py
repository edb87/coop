import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

upDown = 1
pin="P9_14"

print PWM.start(pin, 0, 1000, 0)
for i in range(0,1000):
  PWM.set_duty_cycle(pin, i/float(10))
  sleep(.01)

