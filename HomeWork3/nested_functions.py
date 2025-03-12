first_number= int(input("Введите первое число:"))
second_number= int(input("Введите второе число"))
opertion= input("Выберите операцию (+, -, *, /):")

if opertion == "+":
    result = first_number + second_number
elif opertion == "-":
    result = first_number - second_number
elif opertion == "*":
    result = first_number * second_number
elif opertion == "/":
    result = first_number / second_number
    if second_number !=0:
        result = "Ошибка, делить на 0 нельзя!"
else: result = "Ошибка: неверная операция!"
print("Результат:", result)




