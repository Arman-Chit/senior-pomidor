bug_reports = [
    {"title": "Ошибка 1", "priority": "High"},
    {"title": "Ошибка 2", "priority": "Low"},
    {"title": "Ошибка 3", "priority": "Medium"},
    {"title": "Ошибка 4", "priority": "Critical"},
    {"title": "Ошибка 5", "priority": "Trivial"}
]

def add_bug():
    title = input("Введите заголовок бага: ")
    priority = input("Введите приоритет (High, Low, Medium, Critical, Trivial): ").capitalize()
    if priority not in ["High", "Low", "Medium", "Critical", "Trivial"]:
        print("Некорректный приоритет! Приоритет должен быть 'High', 'Low', 'Medium', 'Critical', 'Trivial'.")
        return
    bug_reports.append({"title": title, "priority": priority})
    print(f"Добавлен новый баг: {title} — {priority}")

def remove_low_priority_bug():
    low_priority_bug = next((bug for bug in bug_reports if bug["priority"] == "Low"), None)
    if low_priority_bug:
        bug_reports.remove(low_priority_bug)
        print(f"Удален баг с низким приоритетом: {low_priority_bug['title']} — {low_priority_bug['priority']}")
    else:
        print("Нет багов с приоритетом 'Low' для удаления.")

def sort_bugs():
    priority_order = {"High": 1,"Low": 2,"Medium": 3, "Critical": 4, "Trivial": 5}
    bug_reports.sort(key=lambda bug: priority_order[bug["priority"]])
    print("Баги отсортированы по приоритету.")

def display_bugs():
    if not bug_reports:
        print("Нет багов для отображения.")
        return
    print("Список багов:")
    for bug in bug_reports:
        print(f"{bug['title']} — {bug['priority']}")

def menu():
    while True:
        print("\nМеню:")
        print("1. Показать все баги")
        print("2. Добавить новый баг")
        print("3. Удалить баг с низким приоритетом")
        print("4. Отсортировать баги по приоритету")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == "1":
            display_bugs()
        elif choice == "2":
            add_bug()
        elif choice == "3":
            remove_low_priority_bug()
        elif choice == "4":
            sort_bugs()
        elif choice == "5":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    menu()
