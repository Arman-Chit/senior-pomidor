#Задача 1
w= int(input("Введите длину прямоугольника: "))
h= int(input("Введите ширину прямоугольника: "))

def rectangle_area(width, height):
    return width * height
print(f"Площадь прямоугольника с шириной {w} и длиной {h} равна: {rectangle_area(w, h)}")


#Задача 2
seconds = int(input("Введите количество секунд: "))
def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds
hours, minutes, remaining_seconds = convert_seconds(seconds)
print(f'В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы)')


Задача 3
number = int(input("Введите число: "))
exponent = int(input("Введите степень: "))

def power_of(number, exponent):
    return number ** exponent
print(f'Число {number} в степени {exponent} равно {power_of(number, exponent)} ')


#Задача 4
def count_items(*args):
    count =len(args)
    print(f'Количество переданнных элементов: {count}.')
    return count
count_items(1, 2, 3, 4, 5)
count_items("apple", "banana", "cherry")

def count_items(*args):
    count = len(args)
    print(f"Количество переданных элементов: {count}")

count_items(1,2,3,4,5)