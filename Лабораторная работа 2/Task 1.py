money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
count=0
while spend<money_capital+salary:
    money_capital -= spend
    money_capital += salary
    spend += (spend * increase)

    count += 1


print("Количество месяцев, которое можно протянуть без долгов:", count)
