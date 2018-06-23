import RPi.GPIO as GPIO
import time
import datetime
import os

#set GPIOS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT) #Relay for Power

try:
    while True:
            GPIO.output(24, GPIO.HIGH)
			time.sleep(10) #to avoid multiple detection
			GPIO.output(24, GPIO.LOW)
except:
    GPIO.cleanup()



