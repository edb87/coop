import Adafruit_BBIO.GPIO as GPIO

lower_pin = "P8_7"
GPIO.setup(lower_pin, GPIO.OUT)
GPIO.output(lower_pin, GPIO.LOW)
GPIO.cleanup()
