coffee_seeds_num = int(input("Сколько зерен?"))
if coffee_seeds_num == 0:
    print("Это не кофе")
elif coffee_seeds_num == 1 or coffee_seeds_num == 2:
    print("Не крепкий кофе")
elif coffee_seeds_num == 3 or coffee_seeds_num == 4:
    print("Крепкий кофе")
else:
    print("Очень крепкий кофе")

sugar_num = int(input("Сколько сахара?"))
if sugar_num == 0:
    print("Кофе без сахара")
else:
    print(f"Добавляю {sugar_num} кубиков кофе")

milk = int(input("Добавить молоко?"))
if milk:
    print("Делаю латте")
else:
    print("Делаю американо")

print(f"Ваш заказ: Количество кофейных зерен:{coffee_seeds_num}\t Количество кубиков сахара:{sugar_num}\t Молоко:{milk}")
