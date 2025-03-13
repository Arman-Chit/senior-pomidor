#Задача 1
s= input("Введите слово: ")
def char_frequency(s):
    dictionary = {}

    for char in s:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary
print(char_frequency(s))


#Задача 2
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dicts(dict1, dict2))


#Задача 3
def dict_to_lists(my_dict):
    keys_list = list(my_dict.keys()
    values_list = list(my_dict.values())
    return keys_list, values_list

my_dict = {"a": 1, "b": 2, "c": 3}
print(dict_to_lists(my_dict))


#Задача 4
def group_by_first_letter(strings):
    result = {}
    for word in strings:
        first_letter = word[0]
        if first_letter not in result:
            result[first_letter] = []
        result[first_letter].append(word)
    return result

strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
print(group_by_first_letter(strings))


#Задача 5
def extract_subdict(my_dict, keys):
    return {key: my_dict[key] for key in keys if key in my_dict}

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
keys = ["a", "c"]
print(extract_subdict(my_dict, keys))
