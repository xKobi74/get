import RPi.GPIO as GPIO

btn = 16
led = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, GPIO.input(btn))

