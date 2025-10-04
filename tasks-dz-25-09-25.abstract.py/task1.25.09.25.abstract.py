# Иерархия сотрудников и задачи проекта
#
# Требования: Создайте систему классов для управления
# сотрудниками, задачами и
#
# проектами в компании
# ;F Создайте абстрактный класс Employee с атрибутами:
#
# ◦ Имя
#
# ◦ Роль (менеджер, разработчик и т.д.)
#
# ◦ Метод work(), который будет реализован в подклассах для
# выполнения конкретных обязанностей
# V# Создайте классы для разных типов сотрудников:
#
# ◦ Developer (разработчик): реализуйте метод work() для
# выполнения программирования.
#
# ◦ Tester: реализуйте метод work() для тестирования кода.
#
# ◦ Manager: метод work() будет управлять командойF
# # Создайте класс Task, который содержит задачу и ссылку
# на сотрудника, который её выполняет
# # Создайте класс Project, который содержит несколько
# задач и сотрудников.
#
# Перегрузите операторы сравнения для сотрудников (==, >, <),
# чтобы можно было сравнивать сотрудников по количеству
# выполненных задач.
#
# Используйте множественное наследование, например, для
# создания класса LeadDeveloper, который является
# одновременно разработчиком и менеджером, чтобы он мог
# выполнять обе роли (программировать и
#
# управлять командой).

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name
        self.role = "Работодатель"
        self.completed_tasks = 0

    @abstractmethod
    def work(self):
        pass

    def __eq__(self, other):
        return self.completed_tasks == other.completed_tasks

    def __gt__(self, other):
        return self.completed_tasks > other.completed_tasks

    def __lt__(self, other):
        return self.completed_tasks < other.completed_tasks

class Developer(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Разработчик"

    def work(self):
        print(f"{self.name} пишет код")
        self.completed_tasks += 1

class Tester(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Тестировщик"

    def work(self):
        print(f"{self.name} тестирует код")
        self.completed_tasks += 1

class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Менеджер"

    def work(self):
        print(f"{self.name} руководит командой.")

class LeadDeveloper(Developer, Manager):
    def __init__(self, name):
        Developer.__init__(self, name)  # Инициализация Developer
        Manager.__init__(self, name)     # Инициализация Manager
        self.role = "Главный разработчик"

class Task:
    def __init__(self, description):
        self.description = description
        self.employee = None

    def assign_employee(self, employee):
        self.employee = employee

    def perform_task(self):
        if self.employee:
            print(f"Задание: {self.description}")
            self.employee.work()
        else:
            print("Ни один сотрудник не назначен на выполнение этой задачи!")

class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.employees = []

    def add_task(self, task):
        self.tasks.append(task)

    def add_employee(self, employee):
        self.employees.append(employee)

    def manage_project(self):
        for task in self.tasks:
            task.perform_task()

# Пример использования

# Создание сотрудников
dev1 = Developer("Алиса")
dev2 = Developer("Гриша")
tester = Tester("Лариса")
manager = Manager("Давид")
lead_dev = LeadDeveloper("Ева")

# Создание задач
task1 = Task("Написать функцию А")
task2 = Task("Протестировать функцию А")
task3 = Task("Проверка кода")

# Присвоение задач
task1.assign_employee(dev1)
task2.assign_employee(tester)
task3.assign_employee(lead_dev)

# Создание проекта и добавление задач и сотрудников
project = Project("Проект А")
project.add_task(task1)
project.add_task(task2)
project.add_task(task3)
project.add_employee(dev1)
project.add_employee(tester)
project.add_employee(lead_dev)

# Управление проектом
project.manage_project()

# Сравнение сотрудников по количеству выполненных задач
print(f" {dev1.name} сделала столько-же как и  {dev2.name}? -> {dev1 == dev2}")
print(f" {dev1.name} сделала больше чем {dev2.name}? -> {dev1 > dev2}")
print(f" {dev1.name} сделала меньше чем {dev2.name}? -> {dev1 < dev2}")