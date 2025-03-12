number = int(input("Введите число: "))
total_sum = 0
print("Числа:", end=" ")

for i in range(1, number + 1):
    print(i, end=" ")
    total_sum += i

print()
print(f"Сумма чисел: {total_sum}")