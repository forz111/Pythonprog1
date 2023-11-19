import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = np.unique(iris[:, 4])
count = len(species)

print("Уникальные значения в столбце species:")
print(species)
print(f"Количество уникальных значений: {count}")
