
import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN) #IR Sensor Input
GPIO.setwarnings(False)
try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(18):
            print "Activity Detected!!"
            print datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            #GPIO.setup(24, GPIO.OUT)
            #GPIO.output(24, GPIO.HIGH)
            time.sleep(1)
            #GPIO.output(24, GPIO.LOW)
            time.sleep(5) #to avoid multiple detection
            time.sleep(0.1) #loop delay, should be less than detection delay
            #os.system('clear')
            #GPIO.output(24, GPIO.LOW)

except:
    GPIO.cleanup()
