import datetime as dt
from time import sleep
from time import time

start_time = 0
end_time = 0


sleep(1)

try:
  while True:

    #Read response time
    start_time = time()
    tt1 = dt.datetime.now()

    sleep(.02)

    end_time = time()
    tt2 = dt.datetime.now()


    #Calculate distance -- pulse width (uS) / 148 = distance in inches
    print 'tt time delta mesaured - '
    print (tt2-tt1).microseconds,'uS'
    
    print 'time() delta measured - '
    print (end_time-start_time)
    print 'Pausing....\n'
    sleep(5)

except KeyboardInterrupt, e:
  print "Exiting: %s" % e
