import numpy as np
from itertools import groupby


def run_length_encoding(x):
    x = x.tolist()

    groups = [(len(list(group)), key) for key, group in groupby(x)]

    numbers = [group[1] for group in groups]
    counts = [group[0] for group in groups]

    numbers = np.array(numbers)
    counts = np.array(counts)

    return numbers, counts


x = np.array([1, 1, 2, 2, 2, 2, 2, 2, 4, 3, 3, 3, 5])
numbers, counts = run_length_encoding(x)
print(numbers)
print(counts)
