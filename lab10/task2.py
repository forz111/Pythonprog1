import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

axs[0, 0].plot(np.sin(3 * t), np.sin(2 * t))
axs[0, 0].set_title('3:2')

axs[0, 1].plot(np.sin(3 * t), np.sin(4 * t))
axs[0, 1].set_title('3:4')

axs[1, 0].plot(np.sin(5 * t), np.sin(4 * t))
axs[1, 0].set_title('5:4')

axs[1, 1].plot(np.sin(5 * t), np.sin(6 * t))
axs[1, 1].set_title('5:6')

for ax in axs.flat:
    ax.label_outer()

plt.show()
