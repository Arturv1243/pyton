#Task2. Разработайте программу для учёта времени учебы за
# неделю. Программа должна позволять пользователю ввести
# количество учебных дней (не более семи), а затем для
# каждого дня вводить количество часов, посвящённых учёбе.
# Программа должна обрабатывать ошибки ввода, такие как
# ввод нечисловых значений и отрицательных чисел, и
# запрашивать повторный ввод при необходимости.

def get_study_days():
    while True:
        try:
            days = int(input("Введите количество учебных дней (не более 7): "))
            if 1 <= days <= 7:
                return days
            else:
                print("Ошибка: Введите положительное число от 1 до 7.")
        except ValueError:
            print("Ошибка: Пожалуйста, введите целое число.")

def get_study_hours(days):
    study_hours = []
    for i in range(1, days + 1):
        while True:
            try:
                hours = float(input(f"Введите количество часов учебы в день {i}: "))
                if hours >= 0:
                    study_hours.append(hours)
                    break
                else:
                    print("Ошибка: Число часов не может быть отрицательным.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите число.")
    return study_hours

def main():
    num_days = get_study_days()
    study_hours = get_study_hours(num_days)

    print("\nУчет времени учебы за неделю:")
    for i in range(num_days):
        print(f"День {i + 1}: {study_hours[i]} часов")

if __name__ == "__main__":
    main()