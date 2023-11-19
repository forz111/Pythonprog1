import numpy as np
from scipy.stats import multivariate_normal
import timeit


def log_pdf_multivariate_normal(X, m, C):
    D = X.shape[1]  # Размерность
    det_C = np.linalg.det(C)  # Определитель матрицы ковариаций
    inv_C = np.linalg.inv(C)  # Обратная матрица ковариаций

    constant = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(det_C)
    X_minus_m = X - m
    exponent = -0.5 * np.sum(np.dot(X_minus_m, inv_C) * X_minus_m, axis=1)

    log_pdf = constant + exponent

    return log_pdf


X = np.random.randn(1000, 2)  # Точки X
m = np.array([0, 0])  # Мат. ожидание
C = np.array([[1, 0], [0, 1]])  # Матрица ковариаций

log_pdf = log_pdf_multivariate_normal(X, m, C)
scipy_log_pdf = multivariate_normal(m, C).logpdf(X)

print(f"Логарифм плотности многомерного нормального распределения (numpy):\n {log_pdf}\n")

print(f"Логарифм плотности многомерного нормального распределения (scipy):\n {scipy_log_pdf}")

numpy_time = timeit.timeit(lambda: log_pdf_multivariate_normal(X, m, C), number=1000)

scipy_time = timeit.timeit(lambda: multivariate_normal(m, C).logpdf(X), number=1000)

print(f"Время работы NumPy: {numpy_time}")
print(f"Время работы SciPy: {scipy_time}")
