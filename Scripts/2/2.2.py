import RPi.GPIO as GPIO
from time import sleep


dac = [10, 9, 11, 5, 6, 13, 19, 26]

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(dac, GPIO.OUT)

def out(x):
    s = bin(x)[2:][::-1]
    print(s)
    num = [0] * 8
    for i in range(len(s)):
        num[i] = int(s[i])
    GPIO.output(dac, num)
    sleep(10)

init()
out(118)
GPIO.cleanup()
