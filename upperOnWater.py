import Adafruit_BBIO.GPIO as GPIO
from time import sleep

lower_pin = "P8_15"
GPIO.setup(lower_pin, GPIO.OUT)
GPIO.output(lower_pin, GPIO.HIGH)
sleep(1000)
GPIO.cleanup()
