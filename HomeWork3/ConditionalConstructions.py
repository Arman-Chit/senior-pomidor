# Задача 1
score = int(input("Введите ваш балл: "))
def check_score(score):
    if score >= 90 and score <= 100:
        print(f"Оценка за {score} баллов: Отлично")
    elif score >= 75 and score <= 89:
        print(f"Оценка за {score} баллов: Хорошо")
    elif score >= 50 and score <= 74:
        print(f"Оценка за {score} баллов: Удовлетворительно")
    else:
        print(f"Оценка за {score} баллов: Неудовлетворительно")
check_score(score)


# Задача 2
number = int(input("Введите число: "))
print(f"Число {number} является четным" if number % 2 == 0 else f"Число {number} является нечетным")


# Задача 3
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
def find_max(num1, num2):
    if num1>num2:
        return num1
    else:
        return num2
max_number = find_max(num1,num2)
print(f"Максимальное из чисел {num1} и {num2}: {max_number}")


# Задача 4
number = int(input("Введите число: "))
def check_number(number):
    if number > 0:
        if number % 2==0:
            print(f"Число {number} положительное и чётное.")
    else:
        print(f"Число {number} отрицательное")
check_number(number)


#Задача 5
user_string = input("Введите строку: ")
user_length = int(input("Введите длину для проверки: "))
def check_string_length(string, length):
    if len(string) > length:
        print(f'Длина строки "{user_string}" достаточная.')
    else:
        print(f'Строка "{user_string}" слишком короткая.')
check_string_length(user_string, user_length)