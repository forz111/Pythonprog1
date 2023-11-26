import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.sin(2 * x)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
l1, = plt.plot(x, y1, label='Волна 1')
l2, = plt.plot(x, y2, label='Волна 2')
l3, = plt.plot(x, y1 + y2, label='Сумма волн', color='r')
plt.legend(loc='upper right')

axcolor = 'white'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Частота', 0.1, 30.0, valinit=1)
samp = Slider(axamp, 'Амплитуда', 0.1, 10.0, valinit=1)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l1.set_ydata(amp * np.sin(freq * x))
    l2.set_ydata(amp * np.sin(2 * freq * x))
    l3.set_ydata(amp * np.sin(freq * x) + amp * np.sin(2 * freq * x))
    fig.canvas.draw_idle()


sfreq.on_changed(update)
samp.on_changed(update)

plt.show()
