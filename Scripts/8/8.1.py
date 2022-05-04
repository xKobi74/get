import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

with open("settings.txt") as f:
    params = list(map(float, f.read().split("\n")))
    diskr = params[0] #Гц
    vstep = params[1] / 1000 #Вольт
yarr = np.loadtxt("data.txt", int)
yarr = yarr * vstep
xarr = np.arange(0, len(yarr))
xarr = xarr / diskr 
k = int(diskr/1.5)
i = np.arange(0, int(len(yarr) / k)) * k

fig, ax = plt.subplots()
fig.set_figwidth(16)
fig.set_figheight(12)

ax.scatter(xarr[i], yarr[i], color="blue", marker="o", s=40)
ax.plot(xarr, yarr, color="blue", linewidth=1, alpha=0.5)
plt.xlim([0, 85])
plt.ylim([0, 3.5])

plt.title(label="Заряд-разрялная кривая конденсатора в RC-цепи", fontsize=20)
plt.xlabel("t, с", fontsize=20)
plt.ylabel("U, В", fontsize=20)
ax.legend(["U(t)"], fontsize=20)

ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)


ax.grid(which='major', color = 'black')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = ':')

ax.text(10, 1, "Время заряда: 41,4с\nВремя разряда: 40,5с", fontsize=20)

plt.savefig("grath.svg", dpi=400)
plt.show()