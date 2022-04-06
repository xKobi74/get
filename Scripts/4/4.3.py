import RPi.GPIO as GPIO
from time import sleep


dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
led = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

p = GPIO.PWM(12, 0.5)
p.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()