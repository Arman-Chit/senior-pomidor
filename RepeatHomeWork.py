# Задача: "Наибольший общий префикс (приставка)"
# Условие:
# Напишите функцию, которая находит наибольший общий префикс среди массива строк.
#
# Если общего префикса нет, верните пустую строку "".
#
# Пример 1:
# Вход: strs = ["flower", "flow", "flight"]
# Выход: "fl"
# Объяснение: Наибольший общий префикс для всех строк — это "fl".
#
# Пример 2:
# Вход: strs = ["dog", "racecar", "car"]
# Выход: ""
# Объяснение: Среди данных строк нет общего префикса.

def max_prefix(word_list):
    common_prefix = []
    min_len = len(min(word_list, key=len))
    for i in range(min_len):
        temp_prefix = set()
        for word in word_list:
            temp_prefix.add(word[:i])
        if len(temp_prefix) == 1:
            common_prefix = list(temp_prefix)[0]
    return common_prefix


strs = ["flower", "flow", "flight"]
print('"' + max_prefix(strs) + '"')

