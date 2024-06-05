import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


def monte_carlo_integration(func, a, b, n=100000):

    x_rand = np.random.uniform(a, b, n)
    y_rand = func(x_rand)

    # Обчислення площі прямокутника, що обмежує функцію
    rectangle_area = (b - a) * np.max(y_rand)

    # Обчислення площі під кривою (інтеграл)
    integral_approx = rectangle_area * np.mean(y_rand)
    return integral_approx

# Обчислення інтеграла
integral_mc = monte_carlo_integration(f, a, b)
print(f"Наближене значення інтеграла (Монте-Карло): {integral_mc:.4f}")


integral_quad, _ = spi.quad(f, a, b)
print(f"Інтеграл (quad): {integral_quad:.4f}")
