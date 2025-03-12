bug_reports = [
    {"title": "Ошибка 1", "priority": "High"},
    {"title": "Ошибка 2", "priority": "Low"},
    {"title": "Ошибка 3", "priority": "Medium"},
    {"title": "Ошибка 4", "priority": "Critical"},
    {"title": "Ошибка 5", "priority": "Trivial"}
]


def add_bug(title, priority):
    """Добавляет новый баг в список, если приоритет корректный."""
    priority = priority.capitalize()
    valid_priorities = ["High", "Low", "Medium", "Critical", "Trivial"]
    if priority not in valid_priorities:
        print("Некорректный приоритет! Доступные: High, Low, Medium, Critical, Trivial.")
        return

    bug_reports.append({"title": title, "priority": priority})
    print(f"Добавлен новый баг: {title} — {priority}")


def remove_low_priority_bug():
    """Удаляет первый найденный баг с приоритетом 'Low'."""
    for bug in bug_reports:
        if bug["priority"] == "Low":
            bug_reports.remove(bug)
            print(f"Удален баг с низким приоритетом: {bug['title']} — {bug['priority']}")
            return
    print("Нет багов с приоритетом 'Low' для удаления.")


def sort_bugs():
    """Сортирует баги по приоритету: Critical > High > Medium > Low > Trivial."""
    priority_order = {"Critical": 1, "High": 2, "Medium": 3, "Low": 4, "Trivial": 5}
    bug_reports.sort(key=lambda bug: priority_order[bug["priority"]])
    print("Баги отсортированы по приоритету.")


# Тестирование функций:
add_bug("Ошибка 6", "High")  # Добавление бага
remove_low_priority_bug()  # Удаление бага с Low
sort_bugs()  # Сортировка
print(bug_reports)  # Вывод списка багов
