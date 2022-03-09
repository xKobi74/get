import RPi.GPIO as GPIO
from time import sleep

ledPins = [21, 20, 16, 12, 7, 8, 25, 24]

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for pin in ledPins:
        GPIO.setup(pin, GPIO.OUT)

def runningLight(cyclesNumber, period):
    state = [1] + [0] * (len(ledPins) - 1)
    for i in range(cyclesNumber * len(ledPins)):
        GPIO.output(ledPins, state)
        sleep(period)
        state[::] = [state[-1]] + state[:-1]


init()
runningLight(3, 0.2)
GPIO.cleanup()
