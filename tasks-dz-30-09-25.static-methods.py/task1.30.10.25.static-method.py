# Описание задачи: создайте программу, которая управляет
# данными о студентах и их средних оценках, используя методы
# экземпляра, методы класса и статические методы. Программа
# должна:
# 1. Позволять добавлять студентов с именем и списком их
# оценок.
# 2. Вычислять и выводить среднюю оценку студента.
# 3. Вычислять и выводить среднюю оценку всех студентов с
# помощью метода класса.
# 4. Проверять, является ли оценка допустимой (от 1 до 5), с
# помощью статического метода.
# Указания:
# 1. Используйте метод экземпляра для добавления студентов и
# вычисления средней оценки для каждого студента.
# 2. Используйте метод класса для вычисления средней оценки
# всех студентов.
# 3. Реализуйте статический метод для проверки допустимости
# оценки.
# 4. Данные о студентах должны храниться в списке в классе.
# 5. Предусмотрите обработку ошибок, если передаётся
# некорректная оценка.
# Ожидаемый результат:
# 1. Программа запрашивает действия у пользователя:
# 2. Добавить нового студента.
# 3. Добавить оценки студенту.
# 4. Вывести среднюю оценку студента.
# 5. Вывести среднюю оценку всех студентов.
# 6. Проверить допустимость оценки.
# 2. Программа корректно вычисляет средние значения.
# 3. При вводе недопустимой оценки (например, 6 или 0)
# программа выдаёт предупреждение.

class Student:
    # Хранит список всех студентов
    students = []

    def __init__(self, name):
        self.name = name
        self.grades = []
        Student.students.append(self)

    def add_grade(self, grade):
        if Student.is_valid_grade(grade):
            self.grades.append(grade)
        else:
            print(f"Оценка {grade} недопустима. Пожалуйста, введите значение от 1 до 5.")

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    @classmethod
    def average_grade_all(cls):
        total_grades = []
        for student in cls.students:
            total_grades.extend(student.grades)
        if not total_grades:
            return 0
        return sum(total_grades) / len(total_grades)

    @staticmethod
    def is_valid_grade(grade):
        return 1 <= grade <= 5


def main():
    while True:
        print("\nМеню:")
        print("1. Добавить нового студента")
        print("2. Добавить оценки студенту")
        print("3. Вывести среднюю оценку студента")
        print("4. Вывести среднюю оценку всех студентов")
        print("5. Проверить допустимость оценки")
        print("6. Выйти")

        choice = input("Выберите действие (1-6): ")

        if choice == '1':
            name = input("Введите имя студента: ")
            Student(name)
            print(f"Студент '{name}' добавлен.")

        elif choice == '2':
            name = input("Введите имя студента: ")
            for student in Student.students:
                if student.name == name:
                    grade = int(input("Введите оценку (1-5): "))
                    student.add_grade(grade)
                    print(f"Оценка {grade} добавлена студенту '{name}'.")
                    break
            else:
                print(f"Студент '{name}' не найден.")

        elif choice == '3':
            name = input("Введите имя студента: ")
            for student in Student.students:
                if student.name == name:
                    avg = student.average_grade()
                    print(f"Средняя оценка студента '{name}': {avg:.2f}")
                    break
            else:
                print(f"Студент '{name}' не найден.")

        elif choice == '4':
            avg_all = Student.average_grade_all()
            print(f"Средняя оценка всех студентов: {avg_all:.2f}")

        elif choice == '5':
            grade = int(input("Введите оценку для проверки (1-5): "))
            if Student.is_valid_grade(grade):
                print(f"Оценка {grade} допустима.")
            else:
                print(f"Оценка {grade} недопустима. Пожалуйста, введите значение от 1 до 5.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == '__main__':
    main()