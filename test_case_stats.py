days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
test_cases = []

for day in days:
    count = int(input(f"Введите количество тест-кейсов за {day}: "))
    test_cases.append(count)

total_tests = sum(test_cases)
average_tests = total_tests / len(days)

print("\n--- Итоговые результаты ---")
print(f"Общее количество тестов за неделю: {total_tests}")
print(f"Среднее количество тестов в день: {average_tests:.2f}")
if average_tests > 10:
    print("Отличная работа!")
else:
    print("Попробуйте улучшить результат.")
