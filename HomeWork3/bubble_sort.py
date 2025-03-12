numbers = input("Введите числа через запятую: ").split(',')
numbers = [int(num) for num in numbers]
numbers.sort()
print(f"Отсортированный список: {numbers}")
