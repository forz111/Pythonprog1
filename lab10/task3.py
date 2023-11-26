import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

t = np.linspace(0, 2 * np.pi, 1000)
line, = ax.plot(np.sin(t), np.sin(t))


def animate(i):
    line.set_ydata(np.sin(i * t))
    return line,


ani = animation.FuncAnimation(fig, animate, interval=20, blit=True, save_count=50)

plt.show()
