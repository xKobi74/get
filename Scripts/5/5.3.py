import RPi.GPIO as GPIO
from time import sleep


delay = 0.01
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
led = [21, 20, 16, 12, 7, 8, 25, 24][::-1]
comp = 4
troyka = 17


def adc():
    cur = [0] * len(dac)
    for i in range(len(dac)):
        cur[i] = 1
        GPIO.output(dac, cur)
        sleep(delay)
        if not GPIO.input(comp):
            cur[i] = 0
    ans = 0
    mult = 1
    for i in range(len(dac) - 1, -1, -1):
        ans += cur[i] * mult
        mult *= 2
    return ans

def display(x):
    x = int((x + len(led) - 1) / 256 * len(led))
    GPIO.output(led, [1] * x + [0] * (len(led) - x))


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

try:
    while 1:
        x = adc()
        display(x)
finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()