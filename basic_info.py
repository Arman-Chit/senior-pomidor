name = input("Введите ваше имя: ")
profession = input("Введите вашу профессию: ")
experience = input("Сколько лет вы работаете в QA? ")
variable_answer = input("Что такое переменная? ")
if "хранит" in variable_answer.lower() or "значение" in variable_answer.lower():
    response = "Отлично! Вы хорошо понимаете основы программирования."
else:
    response = "Переменная — это именованное хранилище данных в программе. Например: x = 10."

print("\n--- Итоговая информация ---")
print(f"Имя: {name}")
print(f"Профессия: {profession}")
print(f"Опыт работы в QA: {experience} лет")
print(response)
