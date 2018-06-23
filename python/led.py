
import RPi.GPIO as GPIO+
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

try:
    while True:
			GPIO.setup(19, GPIO.OUT)
			GPIO.setup(26, GPIO.OUT)
			GPIO.output(19, GPIO.HIGH)
			GPIO.output(26, GPIO.HIGH)
            time.sleep(5) 
            GPIO.output(19, GPIO.LOW)
            GPIO.output(26, GPIO.LOW)
			time.sleep(15) 
except:
    GPIO.cleanup()
