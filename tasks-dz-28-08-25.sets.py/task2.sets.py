def manage_participants():
    participants = {}  # 1. Начинаем с пустого словаря участников
    while True:
        command = input("Введите команду (add, remove, list, exit для выхода): ").lower()
        if command == "add":
            name = input("Введите имя участника: ")
            surname = input("Введите фамилию участника: ")
            interests_str = input("Введите интересы участника через запятую (например, музыка, спорт): ")
            interests = set(interest.strip() for interest in interests_str.split(','))

            # 2. Ключ - кортеж (имя, фамилия), значение - множество интересов
            participant_key = (name.capitalize(), surname.capitalize())
            participants[participant_key] = interests
            print(f"Участник {name} {surname} добавлен в реестр.")

        elif command == "remove":
            name = input("Введите имя участника для удаления: ")
            surname = input("Введите фамилию участника для удаления: ")
            participant_key_to_remove = (name.capitalize(), surname.capitalize())

            # 7. Обработка ошибок: проверка существования участника
            if participant_key_to_remove in participants:
                del participants[participant_key_to_remove]
                print(f"Участник {name} {surname} удален из реестра.")
            else:
                print(f"Ошибка: Участник {name} {surname} не найден в реестре.")

        elif command == "list":
            if not participants:
                print("Реестр участников пуст.")
            else:
                print("\n--- Список участников ---")
                # 5. Просмотр всех участников с их интересами
                for (name, surname), interests in participants.items():
                    print(f"Имя: {name}, Фамилия: {surname}")
                    print(f"Интересы: {', '.join(interests) if interests else 'нет интересов'}")
                print("------------------------\n")

        elif command == "exit":
            print("Программа завершена.")
            break # 6. Выход из программы

        else:
            print("Неверная команда. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    manage_participants()