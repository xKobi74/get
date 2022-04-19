import RPi.GPIO as GPIO
from time import sleep, time
import matplotlib.pyplot as plt

#параметры конфигурации устройства
delay = 0.001
vmax = 3.3
levels = 255
dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
led = [21, 20, 16, 12, 7, 8, 25, 24][::-1]
comp = 4
troyka = 17

#функция, возвращающая уровень напряжения на ацп
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

#функция перевода уровня напряжения в собственно напряжение в вольтах
def convert(x):
    return x / levels * vmax

#функция процентного отображения уровня напряжения на блоке светодиодов платы
def display(x):
    print("Текущее напряжение %.3f В" % convert(x))
    x = int((x + len(led) - 1) / 256 * len(led))
    GPIO.output(led, [1] * x + [0] * (len(led) - x))

#настрока портов устройства
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)

try:
    #параметры эксмперимента: уровни максимального и минимального заряда конденсатора, 
    # принимаемые за заряженное и разряженное состояния, соотвественно
    highlevel = 0.97
    lowlevel = 0.02
    #проведение и измерение эксперимента
    value = []
    voltage = 0
    start = time()
    GPIO.output(troyka, 1)
    while voltage < highlevel * vmax:
        level = adc()
        display(level)
        voltage = convert(level)
        value.append(level)
    GPIO.output(troyka, 0)
    while voltage > lowlevel * vmax:
        level = adc()
        display(level)
        voltage = convert(level)
        value.append(level)
    finish = time()

    #оработка результатов
    duration = finish - start
    period = duration / len(value) * 1000
    diskr = 1 / period * 1000
    step = vmax / levels * 1000
    print("Продолжительность эксперимента: %.3f с\nПериод одного измерения: %.3f мс\nЧастота дискретизации: %.3f Гц\nШаг квантования АЦП: %.3f мВ" % (duration, period, diskr, step))
    with open("data.txt", "w") as f:
        f.write("\n".join([str(v) for v in value]))
    with open("settings.txt", "w") as f:
        f.write(str(diskr) + "\n")
        f.write(str(step) + "\n")
    plt.plot(value)
    plt.show()
finally:
    #очистка состояний использкуемых портов перед завершением программы
    GPIO.output(dac, 0)
    GPIO.output(led, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()