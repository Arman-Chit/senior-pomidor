#Задача 1
s1= input("Введите первое значение: ")
s2= input("Введите второе значение: ")
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagram(s1, s2))


#Задача 2
s= input("Введите строку: ")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome(s))

#Задача 3
s= input("Введите предложение: ")
def longest_word(s):
    words = s.split()
    return max(words, key=len)
print(longest_word(s))


#Задача 4
digits = input("Введите 10-значный номер телефона: ")
def format_phone_number(digits):
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
print(format_phone_number(digits))


#Задача 5
s= input("Введите предложение: ")
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result
print(remove_duplicates(s))


#Задача 6
s = input("Введите предложение: ")
def is_unique(s):
    return len(s) == len(set(s))
print(is_unique(s))
