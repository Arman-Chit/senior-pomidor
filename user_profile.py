name = input("Введите ваше имя: ")
profession = input("Введите вашу профессию: ")
tool = input("Введите ваш любимый инструмент для тестирования: ")

print("\n--- Итоговая информация ---")
print(f"Имя: {name}")
print(f"Профессия: {profession}")
if not tool:
    print("Инструмент не указан. Попробуйте снова!")
else:
    print(f"Ваш любимый инструмент: {tool}. Отличный выбор!")



