name= input("Введите ваше имя:")
print(f"Привет,{name}! Добро пожаловать в мир Python!")

def calculate_sum (a,b):
    return a+b

if __name__ == "__main__":
    try:
        a= int(input("Введите первое число:"))
        b= int(input("Введите второе число:"))
        result = calculate_sum (a,b)
        print(f"Сумма чисел {result}")

    except ValueError:
        print("Ошибка: Введите целые числа.")