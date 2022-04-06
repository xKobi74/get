import RPi.GPIO as GPIO
from time import sleep


delay = 0.01
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
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