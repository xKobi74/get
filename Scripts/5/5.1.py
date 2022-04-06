import RPi.GPIO as GPIO
from time import sleep


delay = 0.01
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
comp = 4
troyka = 17


def d2b(x):
    return [int(bin) for bin in (bin(x)[2:]).zfill(8)]

def adc():
    for i in range(2 ** len(dac)):
        GPIO.output(dac, d2b(i))
        sleep(delay)
        if not GPIO.input(comp):
            return i
    return -1


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

try:
    while 1:
        x = adc()
        print("{:} = {:.3f}".format(x, x * 3.3 / 2 ** len(dac)))
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()