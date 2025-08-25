#Создайте программу для управления списком задач.
#Пользователь должен иметь
#возможность добавлять задачи в список и удалять их по
#завершении. Каждая задача представляет собой простую
#строку с описанием.
def display_menu():
    """Отображает меню действий."""
    print("\n--- Меню управления задачами ---")
    print("1. Добавить задачу")
    print("2. Посмотреть список задач")
    print("3. Удалить задачу")
    print("4. Выйти")
    print("------------------------------")

def add_task(task_list):
    """Добавляет новую задачу в список."""
    task = input("Введите описание новой задачи: ")
    task_list.append(task)
    print(f"Задача '{task}' добавлена!")

def view_tasks(task_list):
    """Отображает список всех задач с номерами."""
    if not task_list:
        print("Список задач пуст!")
    else:
        print("\n--- Ваш список задач ---")
        for index, task in enumerate(task_list):
            print(f"{index + 1}. {task}")
        print("------------------------")

def delete_task(task_list):
    """Удаляет задачу из списка по её номеру."""
    view_tasks(task_list)
    if not task_list:
        return

    try:
        task_number = int(input("Введите номер задачи, которую хотите удалить: "))
        if 1 <= task_number <= len(task_list):
            removed_task = task_list.pop(task_number - 1)
            print(f"Задача '{removed_task}' удалена.")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите корректное число.")

def main():
    """Основная функция программы."""
    tasks = []
    while True:
        display_menu()
        choice = input("Выберите действие (1-4): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Программа завершена. Хорошего дня!")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 4.")

if __name__ == "__main__":
    main()