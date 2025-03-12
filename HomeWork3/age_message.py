from datetime import datetime
birth_year = int(input("Введите ваш год рождения: "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Ваш возраст {age}")
if age < 18:
    print("Вы еще молоды, учеба — ваш путь!")
elif 18 <= age <= 65:
    print("Отличный возраст для карьерного роста!")
else:
    print("Пора наслаждаться заслуженным отдыхом!")
