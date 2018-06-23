import RPi.GPIO as GPIO
import time
import datetime
import os

#set GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.IN) #PIR
GPIO.setup(17, GPIO.OUT) #Relay for Power

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            print "Motion Found"
            print datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            GPIO.output(17, GPIO.LOW)
			time.sleep(105) #to avoid multiple detection
			GPIO.output(17, GPIO.HIGH)
except:
    GPIO.cleanup()



