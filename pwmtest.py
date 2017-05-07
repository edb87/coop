import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

foo = 0
upDown = 1
pin="P9_14"

print PWM.start(pin, 0, 100000, 0)
try:
  while True:
    if upDown:
      if abs(foo) >= 99.9:
        upDown=0
      else:
        foo+=.1
    else:
      if abs(foo) <=0.1:
        upDown=1
      else:
        foo-=.1
    sleep(.001)
    PWM.set_duty_cycle(pin, foo)

except KeyboardInterrupt, e:
  print "Exiting: %s" % e
  PWM.set_duty_cycle(pin, 0)
  PWM.stop(pin)
  #PWM.cleanup() 
  print("Bye!")

