import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

upDown = 1
pin="P9_14"

print PWM.start(pin, 0, 1000, 0)
try:
  for i in range(0,1000):
    print i/float(10)
    PWM.set_duty_cycle(pin, i/float(10))
    sleep(.01)
  while True:
    sleep(1)
  """for i in range(1000,0, -1):
    PWM.set_duty_cycle(pin, i/float(10))
    sleep(.001)
  sleep(2)
  PWM.set_duty_cycle(pin, 0)
  """
except KeyboardInterrupt, e:
  print "Exiting: %s" % e
  PWM.set_duty_cycle(pin, 0)
  PWM.stop(pin)
  #PWM.cleanup() 
  print("Bye!")

