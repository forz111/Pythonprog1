import matplotlib.pyplot as plt
import numpy as np

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

count, bins, ignored = plt.hist(s, 30, density=True)

plt.show()
