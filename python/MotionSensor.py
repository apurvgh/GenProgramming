import RPi.GPIO as GPIO
import time
import datetime
import os

#set GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) #PIR
#GPIO.setup(24, GPIO.OUT) #TODO BUzzer 

try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            print "Hey Human, wassup?"
            print datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
            time.sleep(5) #to avoid multiple detection
            time.sleep(0.1) #loop delay, should be less than detection delay
            os.system('clear') #clear the screen to avoid displaying multiple output print

except:
    GPIO.cleanup()



