import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_indices = np.where(x == 0)[0]

max_after_zero = None

for i in zero_indices:
    if i + 1 < len(x):
        if max_after_zero is None or x[i + 1] > max_after_zero:
            max_after_zero = x[i + 1]

print(max_after_zero)
