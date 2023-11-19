import numpy as np

a = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])

indices = np.nonzero(a)

indices_list = indices[0].tolist()

print(f"Список индексов ненулевых элементов: {indices_list}")
