import RPi.GPIO as GPIO
from time import sleep


ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '    '}

def translate(s):
    res = ""
    for c in s.upper():
        res += ENGLISH_TO_MORSE[c] + "   "
    return res

def out(s, pin):
    t = 0.3
    for c in s:
        if c != " ":
            GPIO.output(pin, 1)
            sleep(3 * t if c == "-" else t)
            GPIO.output(pin, 0)
            sleep(t)
        else:
            sleep(t)

led = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

msg = "Privet"
mor = translate(msg)
print(mor)
out(mor, led)