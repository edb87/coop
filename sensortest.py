import Adafruit_BBIO.GPIO as GPIO
import datetime as dt
from time import sleep
from time import time


out_trig_pin="P8_3"
in_echo_pin="P8_4"
start_time = 0
end_time = 0

GPIO.setup(in_echo_pin, GPIO.IN)
GPIO.setup(out_trig_pin, GPIO.OUT)

sleep(1)

try:
  while True:
    #Initiate high pulse for 10 micro seconds
    GPIO.output(out_trig_pin, GPIO.HIGH)
    sleep(.0001)
    GPIO.output(out_trig_pin, GPIO.LOW)

    #Read response time
    GPIO.wait_for_edge(in_echo_pin, GPIO.RISING)
    start_time = dt.datetime.now()
    GPIO.wait_for_edge(in_echo_pin, GPIO.FALLING)
    end_time = dt.datetime.now()

    #Calculate distance -- pulse width (uS) / 148 = distance in inches
    print 'time measured is ',(end_time-start_time).microseconds,'uS'
    print 'Calculated distance is ',((end_time-start_time).microseconds)/148,' inches'
    sleep(10)

except KeyboardInterrupt, e:
  print "Exiting: %s" % e
  GPIO.cleanup()
