grams = 12345                  #2.2.5 Задача 1
kg = grams // 1000
print("В", grams, "граммах содержится", kg, "полных килограмм.")

number = 1234                     #2.2.5 Задача 2
last_digit = number % 10
print(last_digit)

number1 = 15                   #2.2.5 Задача 3
if number1 > 0 and number1 % 2 == 0:
    print("Число", number1, "является положительным и четным.")
else:
    print("Число", number1, "не подходит под условия.")

num = 100                  #2.2.5 Задача 4
if num >= 0 and num <= 100:
    print("Число", num, "находится в пределах диапазона от 0 до 100.")
else:
    print("Число", num, "выходит за пределы диапазона от 0 до 100.")

number = 10                     #2.2.5 Задача 5

if number % 3 != 0:  # Проверка на то, что число не делится на 3
    print(f"Число {number} не кратно 3.")
else:
    print(f"Число {number} кратно 3.")
