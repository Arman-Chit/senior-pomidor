name=input("Введите Ваше имя:")
years= input("Введите сколько лет работаете в QA:")
question =("Что такое переменная?")
print(question)
user_answer =input ("Ваш ответ: ")
if user_answer == "это именованная область памяти":
    print(f"Привет, {name}! Добро пожаловать в мир Python для тестировщиков.")
else :
    print(f"Привет, {name}! Пожалуйста повтори переменные.")