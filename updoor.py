import Adafruit_BBIO.GPIO as GPIO
from time import sleep

upPin = "P8_14"
downPin = "P8_16"
hallUpSensor = "P8_18"
hallDnSensor = "P8_19"

GPIO.setup(upPin,   GPIO.OUT)
GPIO.setup(downPin, GPIO.OUT)
GPIO.setup(hallDnSensor, GPIO.IN)
GPIO.setup(hallUpSensor, GPIO.IN)

if not GPIO.input(hallUpSensor):
  print "Door already up!"
  exit()

GPIO.output(upPin, GPIO.HIGH)
#sleep(22)
GPIO.wait_for_edge(hallUpSensor, GPIO.FALLING)
GPIO.output(upPin, GPIO.LOW)

#GPIO.output("P8_16", GPIO.HIGH)
#GPIO.output("P8_16", GPIO.LOW)

