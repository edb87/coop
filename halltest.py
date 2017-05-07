import Adafruit_BBIO.GPIO as GPIO
from time import sleep


HALL_SENSOR = "P8_18"
hallActive = False 

GPIO.setup(HALL_SENSOR, GPIO.IN)

try:
  while True:
    #Wait for change
    print GPIO.input(HALL_SENSOR)
    sleep(.005)
    """print("Waiting...")
    GPIO.wait_for_edge(HALL_SENSOR, GPIO.BOTH)
    print "Change!" 
    hallActive = GPIO.input(HALL_SENSOR)
    
    if(hallActive == False):
        print("Switch state active, falling edge detected")
    else:
        print("Switch state off, rising edge detected")
    """

except KeyboardInterrupt, e:
  print "Exiting: %s" % e
  GPIO.cleanup()
