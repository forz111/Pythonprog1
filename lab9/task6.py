import numpy as np

a = np.arange(16).reshape(4, 4)

print("Исходный массив:")
print(a)

a[[0, 2]] = a[[2, 0]]

print("Массив после обмена строк:")
print(a)
