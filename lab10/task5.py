import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = (1 / 2) * (x ** 2 + y ** 2)

fig = plt.figure(figsize=(12, 6))

# Первый график
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='gnuplot')
ax1.set_title('График MSE')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')

# График с логарифмической осью Z
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, np.log(z), cmap='gnuplot')
ax2.set_title('График MSE (логарифмическая ось Z)')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('log(Z)')

plt.show()
