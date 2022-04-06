import RPi.GPIO as GPIO


def d2b(x):
    return [int(bin) for bin in (bin(x)[2:]).zfill(8)]


dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

try:
    while 1:
        s = input("Enter number from 0 to 255: ")
        if (s == "q"):
            break
        try:
            x = float(s)
        except:
            print("You should enter number")
            continue
        try:
            x = int(s)
        except:
            print("You should enter integer number")
            continue
        if (x < 0):
            print("Enter positive number")
            continue
        if (x < 0 or x > 255):
            print("Number should be between 0 and 255")
            continue
        GPIO.output(dac, d2b(x))
        print("Current voltage is aproximately equal {:.3f} volts".format(x / 256 * 3.3))
except:
    print("Something went wrong")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
