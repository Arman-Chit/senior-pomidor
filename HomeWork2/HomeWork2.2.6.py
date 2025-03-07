numbers = [1,2,3] #2.2.6 Задача 1
numbers.append(4)
print(numbers)

fruits =["Москва", "Лондон", "Париж"] #2.2.6 Задача 2
fruits.remove("Лондон")
print(fruits)

cities=["Москва", "Питер", "Новосибирск", "Екатеринбург"]#2.2.6 Задача 3
print(cities[2])

numbers=[0,1,2,3,4,5,6,7,8,9]#2.2.6 Задача 4
print(numbers[3:7])

colors=["red","green","blue"]#2.2.6 Задача 5
colors[1]= "yellow"
print(colors)

animals=["cat", "dog", "rabbit", "hamster"]#2.2.6 Задача 6
len_list= len(animals)
print(len_list)

student= {"name":"Ivan", "age": 20}#2.2.6 Задача 7
student["grade"]="A"
print(student)

student= {"name":"Ivan", "age": 20, "greade":"B"}#2.2.6 Задача 8
student["greade"]="A"
print(student)

student= {"name":"Ivan", "age": 20, "greade":"A"}#2.2.6 Задача 9
del student["age"]
print(student)

student= {"name":"Ivan", "age": 20, "greade":"A"}#2.2.6 Задача 10
print(student["name"])

student= {"name":"Ivan", "age": 20, "greade":"A"}#2.2.6 Задача 11
print("greade" in student)

student = {"name" : "Ivan",                     #2.2.6 Задача 12
           "address" :
               { "city" : "Moscow",
                 "street" : "Lenina"
                 }

           }
student["address"]["city"]="Saint Peterbutg"
print(student)

student = {"name" : "Maria",                     #2.2.6 Задача 13
           "grades": [75,82,90]
           }
student["grades"][0]=85
print(student)

student = [ {"name": "Ivan", "age": 20}, {"name": "Petya", "age": 22}] #2.2.6 Задача 14
student[1]["age"] = 23
print(student)

colors=("red","green", "blue")                              #2.2.6 Задача 15
is_green_present = "green" in colors
length = len(colors)
print(f"Наличие 'green': {is_green_present}. Длина кортежа: {length}")