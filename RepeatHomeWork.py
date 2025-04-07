# Даны две строки s и t, состоящие из строчных букв. Строка t получается путем случайного перемешивания строки s с добавлением одного дополнительного символа в случайную позицию.
#
# Найти этот дополнительный символ.
#
# Примеры:
# Вход: s = "abcd", t = "abcde"
# Выход: "e"
#
# Вход: s = "aabbc", t = "abacbb"
# Выход: "c"


# def find_extra_char(s: str, t: str) -> str:
#     return chr(sum(map(ord, t)) - sum(map(ord, s)))
#
# # Примеры вызова:
# print(find_extra_char("abcd", "abcde"))    # e
# print(find_extra_char("aabbc", "abacbb"))  # c

def find_extra_char(s: str, t: str) -> str:
    s_sorted = sorted(s)
    t_sorted = sorted(t)

    for ch1, ch2 in zip(s_sorted, t_sorted):
        if ch1 != ch2:
            return ch2
    return t_sorted[-1]  # если все символы до последнего совпали, то последний — лишний

print(find_extra_char("abcd", "abcde"))      # e
print(find_extra_char("aabbc", "abacbb"))    # c
print(find_extra_char("xyz", "xzyq"))        # q

