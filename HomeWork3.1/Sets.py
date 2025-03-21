#Задача 1
lst = input("Введите значения через запятую: ").split(',')

if all(item.isdigit() for i tem in lst):
    lst = list(map(int, lst))
def get_unique_elements(lst):
    return list(set(lst))

print(get_unique_elements(lst))


#Задача2
lst = input("Введите предложение: ").split(',')

def is_unique_list(lst):
    return len(lst) == len(set(lst))
print(is_unique_list(lst))

#Задача3
s = input("Введите строку: ")
def get_unique_vowels(s):
    vowels = "aeiou"
    s = s.lower()
    unique_vowels = set()

    for char in s:
        if char in vowels:
            unique_vowels.add(char)

    return unique_vowels

print(get_unique_vowels(s))