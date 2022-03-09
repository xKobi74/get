import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

GPIO.output(26, 1)
sleep(0.5)
GPIO.output(26,0)
sleep(0.5)

GPIO.output(26, 1)
sleep(0.5)
GPIO.output(26,0)
sleep(0.5)

GPIO.output(26, 1)
sleep(0.5)
GPIO.output(26,0)
sleep(0.5)

GPIO.output(26, 1)
sleep(0.5)
GPIO.output(26,0)
sleep(0.5)

GPIO.output(26, 1)
sleep(0.5)
GPIO.output(26,0)
sleep(0.5)