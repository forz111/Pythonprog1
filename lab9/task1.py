import numpy as np

matrix = np.genfromtxt('matrix1.txt', delimiter=',')

sum_elements = np.sum(matrix)
max_element = np.max(matrix)
min_element = np.min(matrix)

print("Матрица:")
print(matrix)

print(f"Сумма всех элементов: {sum_elements}")
print(f"Максимальный элемент: {max_element}")
print(f"Минимальный элемент: {min_element}")
