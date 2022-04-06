import RPi.GPIO as GPIO
from time import sleep


def d2b(x):
    return [int(bin) for bin in (bin(x)[2:]).zfill(8)]


dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    period = float(input("Enter period: "))
except:
    print("Restart program and enter correct number")
    GPIO.output(dac, [0] * len(dac))
    GPIO.cleanup()
delay = period / (256 + 254)

try:
    while 1:
        for v in range(256):
            GPIO.output(dac, d2b(v))
            sleep(delay) 
        for v in range(254, 0, -1):
            GPIO.output(dac, d2b(v))
            sleep(delay)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
