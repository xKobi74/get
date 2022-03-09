import RPi.GPIO as GPIO
from time import sleep


aux = [22, 23, 27, 18, 15, 14, 3, 2]
leds = [21, 20, 16, 12, 7, 8, 25, 24]


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(leds, GPIO.OUT)
    GPIO.setup(aux, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def state(pins):
    res = [0] * len(pins)
    for i in range(len(pins)):
        res[i] = GPIO.input(pins[i])
    return res

init()
while True:
    GPIO.output(leds, state(aux))