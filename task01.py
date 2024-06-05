import pulp

# Створення моделі лінійної оптимізації
model = pulp.LpProblem("Максимізація виробництва напоїв", pulp.LpMaximize)

# Змінні рішення: кількість кожного напою
lemonade = pulp.LpVariable("Лимонад", lowBound=0, cat='Integer')
juice = pulp.LpVariable("Фруктовий сік", lowBound=0, cat='Integer')

# Цільова функція: максимізувати загальну кількість напоїв
model += lemonade + juice

# Обмеження:
model += 2 * lemonade + juice <= 100  # Вода
model += lemonade <= 50  # Цукор
model += lemonade <= 30  # Лимонний сік
model += 2 * juice <= 40  # Фруктове пюре

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Оптимальне рішення:")
print("Лимонад:", pulp.value(lemonade))
print("Фруктовий сік:", pulp.value(juice))
print("Загальна кількість напоїв:", pulp.value(model.objective))
