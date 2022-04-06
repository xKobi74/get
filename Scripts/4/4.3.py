import RPi.GPIO as GPIO
from time import sleep


def d2b(x):
    return [int(bin) for bin in (bin(x)[2:]).zfill(8)]


dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
led = 21
pwm = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pwm, GPIO.OUT)
p = GPIO.PWM(pwm, 1000)
p.start(0)

try:
    while 1:
        k = int(input("Enter duty cycle: "))
        p.ChangeDutyCycle(k)
finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    p.stop()
    GPIO.output(pwm, 0)
    GPIO.cleanup()