#Задача 1
number = int(input("Введите число: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
print()
print(f"Сумма чисел от 1 до {number}: {total_sum}")


#Задача 2
numbers = input("Введите числа через запятую: ").split(',')
numbers = [int(num) for num in numbers]

min_number = min(numbers)
print(f"Минимальное число в списке: {min_number}")


#Задача 3
word = input("Введите текст: ")
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    return count


result = count_vowels(word)
print(f"Количество гласных в строке: {result}")


#Задача 4
num = int(input("Количество строк: "))
def print_diamond(rows):
    for i in range(1, rows + 1):
        print("* " * i)

    for i in range(rows - 1, 0, -1):
        print("* " * i)

print_diamond(num)


#Задача 5
def countdown():
     for i in range(10, 0, -1):
         print(i)
     print("Старт!")
countdown()


# Задача 6
def countdown():
    num=10
    while num>0:
        print(num)
        num -=1
    print("Старт!")
countdown()

