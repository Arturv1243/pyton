# Задание: «Система управления библиотекой»
# Описание
# Необходимо смоделировать простую систему учёта книг в библиотеке
# с использованием классов и наследования.
# Требования:
# 1. Создайте базовый класс Item, который будет описывать общий
# объект в библиотеке.
# ◦ Атрибуты:
# ▪ title (название)
# ▪ year (год издания)
# ◦ Метод __str__() для красивого вывода информации.
# 2. Создайте класс-наследник Book, расширяющий
# функциональность:
# ◦ Дополнительные атрибуты:
# ▪ author (автор)
# ▪ pages (количество страниц)
# ◦ Переопределите метод __str__(), чтобы он включал все
# атрибуты.
# 3. Создайте ещё один класс-наследник Magazine:
# ◦ Дополнительные атрибуты:
# ▪ issue (номер выпуска)
# ▪ publisher (издательство)
# ◦ Переопределите метод __str__().
class Item:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Название: {self.title}, Год издания: {self.year}"



class Book(Item):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Книга: {self.title}, Год издания: {self.year}, Автор: {self.author}, Страницы: {self.pages}"





class Magazine(Item):
    def __init__(self, title, year, issue, publisher):
        super().__init__(title, year)
        self.issue = issue
        self.publisher = publisher

    def __str__(self):
        return f"Журнал: {self.title}, Год издания: {self.year}, Выпуск: {self.issue}, Издательство: {self.publisher}"

if __name__ == "__main__":
    # Создание объектов библиотеки
    book = Book("1984", 1949, "Джордж Оруэлл", 328)
    magazine = Magazine("Наука и жизнь", 2023, 5, "Научное издательство")
    print("")
    book1=Book("Дикий Зверь",2020,"Жоэль Диккер",329)
    magazine1=Magazine("Девушка из Италии", 2015,6,"Любовный роман")
    # Вывод информации о книгах и журналах
    print(book)
    print(magazine)
    print(book1)
    print(magazine1)

