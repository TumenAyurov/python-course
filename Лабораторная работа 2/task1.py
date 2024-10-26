money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
budget_month = money_capital + salary
n = budget_month - spend
while n >= 0:
    spend = (spend * increase) + spend
    n = n - spend
    n += salary
    month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
