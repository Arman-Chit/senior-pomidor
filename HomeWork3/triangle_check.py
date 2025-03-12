def check_triangle(a, b, c):
    if a+b>c and b+c>a and a+c>b:
        if a==b==c:
            return "Треугольник Равносторонний"
        elif a==b or b==c or a==c:
            return "Треугольник равнобедренный"
        else:
            return "Треугольник разносторонний"
    else:
        return "Треугольник построить нельзя"

a = float(input("Введите сторону (а): "))
b = float(input("Введите сторону (b): "))
c = float(input("Введите сторону (c): "))
result = check_triangle(a, b, c)
print(result)
