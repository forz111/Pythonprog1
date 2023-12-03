import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t = np.linspace(0, 1, 500, endpoint=False)

square = signal.square(2 * np.pi * 5 * t)

plt.figure()
plt.plot(t, square)
plt.ylim(-2, 2)
plt.show()
