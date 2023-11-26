import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

x = np.linspace(-1, 1, 1000)

plt.figure(figsize=(10, 6))
plt.title('Полиномы Лежандра')

for i in range(1, 8):
    y = legendre(i)(x)
    plt.plot(x, y, label=f'n = {i}')

plt.legend(loc='upper right')
plt.grid(True)
plt.show()
