import numpy as np
import scipy.integrate as sci

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

def mc_integral(a, b, num_samples=10000):
    # Генерація випадкових точок
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, f(b), num_samples)
    
    # Оцінка кількості точок під кривою
    points_under_curve = np.sum(y <= f(x))
    area_ratio = points_under_curve / num_samples
    
    # Оцінка площі під кривою
    total_area = (b - a) * f(b)
    return total_area * area_ratio

if __name__ == "__main__":
    # Обчислення числового інтегралу
    numerical_integral = sci.quad(f, a, b)
    print(f"Числовий інтеграл: {numerical_integral}")

    # Перевірка результатів для різної кількості точок
    num_samples = [100, 1000, 10000, 100000, 1000000, 10000000]
    for sample in num_samples:
        mc_result = mc_integral(a, b, num_samples=sample)
        print(f"Monte Carlo інтеграл ({sample} точок): {mc_result}")
