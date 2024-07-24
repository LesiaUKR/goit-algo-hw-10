import pulp

# Створюємо LP проблему для максимізації
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішень: кількість лимонаду та фруктового соку
lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
juice = pulp.LpVariable('juice', lowBound=0, cat='Integer')

# Цільова функція: максимізація кількості вироблених продуктів
model += lemonade + juice, "Total_Products"

# Обмеження ресурсів
model += 2 * lemonade + juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "LemonJuice_Constraint"
model += 2 * juice <= 40, "FruitPuree_Constraint"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Статус: {pulp.LpStatus[model.status]}")
print(f"Кількість лимонаду: {lemonade.varValue}")
print(f"Кількість фруктового соку: {juice.varValue}")
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")
