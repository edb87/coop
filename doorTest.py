from time import sleep
import Adafruit_BBIO.GPIO as GPIO

hallUpSensor = "P8_18"
hallDnSensor = "P8_19"

GPIO.setup(hallDnSensor, GPIO.IN)
GPIO.setup(hallUpSensor, GPIO.IN)

if not GPIO.input(hallDnSensor):
  print "Door down!"
else :
  print "Door NOT down..."
if not GPIO.input(hallUpSensor):
  print "Door up!"
else :
  print "Door NOT up..."

