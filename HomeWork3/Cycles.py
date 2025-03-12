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
