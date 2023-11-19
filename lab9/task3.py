import numpy as np

array = np.random.normal(size=(10, 4))
print(array)

min_value = np.min(array)
print(f'Минимальное значение: {min_value}')

max_value = np.max(array)
print(f'Максимальное значение: {max_value}')

mean_value = np.mean(array)
print(f'Среднее значение: {mean_value}')

std_dev = np.std(array)
print(f'Стандартное отклонение: {std_dev}')

first_5_rows = array[:5]
print(first_5_rows)
