# Task 1
s = input("Please input a string")
if len(s) < 2:
    print("Empty String")
else:
    print(s[:2]+s[-2:])
    print()

# Task 2
phone_number = input("Введите номер телефона")
if len(phone_number) == 10:
    print("Валидный номер телефона")
else:
    print("Неверный номер телефона")


# Task 3
import random
num1 = random.randint(0, 5)
num2 = random.randint(0, 5)
switch = random.randint(0,3)
if switch == 0:
    result = int(input(f"Сколько будет {num1} + {num2}?"))
    if result == num1 + num2:
        print("Верно")
    else:
        print("Неверно")
elif switch == 1:
    result = int(input(f"Сколько будет {num1} - {num2}?"))
    if result == num1 - num2:
        print("Верно")
    else:
        print("Неверно")
elif switch == 2:
    result = int(input(f"Сколько будет {num1} * {num2}?"))
    if result == num1 * num2:
        print("Верно")
    else:
        print("Неверно")
elif switch == 3:
    result = int(input(f"Сколько будет {num1}^{num2}?"))
    if result == num1 ** num2:
        print("Верно")
    else:
        print("Неверно")

# Task 4
name = "vlad"
name_input = input("Введите ваше имя")
if name == name_input.strip().lower():
    print("Вы ввели правильное имя")
else:
    print("Имя неверно")
