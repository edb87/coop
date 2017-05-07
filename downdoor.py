from time import sleep
import Adafruit_BBIO.GPIO as GPIO

upPin = "P8_14"
downPin = "P8_16"
hallUpSensor = "P8_18"
hallDnSensor = "P8_19"

GPIO.setup(upPin,   GPIO.OUT)
GPIO.setup(downPin, GPIO.OUT)
GPIO.setup(hallDnSensor, GPIO.IN)
GPIO.setup(hallUpSensor, GPIO.IN)

#Since we wait 5 seconds after sensing the door is closed to lock it, a closed door doesn't trigger the down sensor. Our best guess is to confirm it is currently open
if GPIO.input(hallUpSensor):
  print "Door not confirmed up, it's probably already down!"
#  exit()
if not GPIO.input(hallDnSensor):
  print "Door already down!"
#  exit()

GPIO.output(downPin, GPIO.HIGH)
GPIO.wait_for_edge(hallDnSensor, GPIO.FALLING)
sleep(5) #Give it 5 extra seconds to lock door once it's down
GPIO.output(downPin, GPIO.LOW)


