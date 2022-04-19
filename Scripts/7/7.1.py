import RPi.GPIO as GPIO
from time import sleep, time
import matplotlib.pyplot as plt

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

def convert(x):
    return x / 255 * 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)

try:
    vmax = 3.3 / 2
    highlevel = 0.97
    lowlevel = 0.02
    value = []
    voltage = 0
    start = time()
    GPIO.output(troyka, 1)
    while voltage < highlevel * vmax:
        level = adc()
        display(level)
        voltage = convert(level)
        value.append(voltage)
    GPIO.output(troyka, 0)
    while voltage > lowlevel * vmax:
        level = adc()
        display(level)
        voltage = convert(level)
        value.append(voltage)
    finish = time()

    duration = finish - start
    period = duration / len(value) * 1000
    diskr = 1 / period * 1000
    step = 3.3 / 255 * 1000
    print("Продолжитеьность эксперимента: %.3f с\nПериод одного измерения: %.3f мс\nЧастота дискретизации: %.3f Гц\nШаг квантования АЦП: %.3f мВ" % (duration, period, diskr, step))
    with open("data.txt", "w") as f:
        f.write("\n".join([str(v) for v in value]))
    with open("settings.txt", "w") as f:
        f.write(str(diskr) + "\n")
        f.write(str(step) + "\n")
    plt.plot(value)
    plt.show()
finally:
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()