#Задача 1
s1= input("Введите первое значение: ")
s2= input("Введите второе значение: ")
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagram(s1, s2))