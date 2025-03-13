#Задача 1
lst = input("Введите значения через запятую: ").split(',')

def remove_duplicates(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(remove_duplicates(lst))


#Задача 2
n = int(input("Введите конечное значение: "))

def generate_squares(n):
    return [i ** 2 for i in range(1, n + 1)]

print(generate_squares(n))


#Задача 3
list1 = input("Введите первое значение через запятую: ").split(',')
list2 = input("Введите второе значение через запятую: ").split(',')

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

def merge_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    set1.update(set2)
    return list(set1)

print(merge_lists(list1, list2))

#Задача 4
lst = input("Введите значение через запятую: ").split(',')
list1 = [int(num) for num in lst]
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted(lst))

#Задача 5
list1 = input("Введите первое значение через запятую: ").split(',')
list2 = input("Введите второе значение через запятую: ").split(',')

list1 = [int(num) for num in list1]
list2 = [int(num) for num in list2]

def merge_lists(list1, list2):
    return [list1[i] + list2[i] for i in range(len(list1))]

print(merge_lists(list1, list2))


