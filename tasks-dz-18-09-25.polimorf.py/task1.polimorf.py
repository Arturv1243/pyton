# Создайте систему для управления заказами в ресторане,
# используя классы для моделирования блюд и заказов.
# 1. Реализуйте классы Dish (блюдо) и Order (заказ).
# Класс Dish должен содержать информацию о названии и цене блюда.
# 2. Класс Order должен хранить информацию о нескольких блюдах, которые
# входят в заказ.
# 3. Создайте несколько классов-наследников от Dish:
# MainDish (основное блюдо), Dessert (десерт) и Drink (напиток). Пусть у
# каждого класса будут специфические свойства (например, наличие
# алкоголя у напитков или вегетарианские блюда).
# 4. Класс Order должен уметь работать с любыми типами блюд, поддерживая
# добавление и удаление блюд различных типов в заказ.
# 5. Перегрузите оператор +, чтобы можно было объединять два объекта Order
# (суммировать заказы).
# 6. Перегрузите оператор >, чтобы сравнивать заказы по общей стоимости.
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class MainDish(Dish):
    def __init__(self, name, price, is_vegetarian=False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def __str__(self):
        veg_str = " (Вегетарианский)" if self.is_vegetarian else ""
        return super().__str__() + veg_str


class Dessert(Dish):
    def __init__(self, name, price, is_gluten_free=False):
        super().__init__(name, price)
        self.is_gluten_free = is_gluten_free



class Drink(Dish):
    def __init__(self, name, price, is_alcoholic=False):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic

    def __str__(self):
        alcohol_str = " (Алкогольное)" if self.is_alcoholic else ""
        return super().__str__() + alcohol_str


class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        self.dishes.remove(dish)

    def total_cost(self):
        return sum(dish.price for dish in self.dishes)

    def __str__(self):
        order_summary = "\n".join(str(dish) for dish in self.dishes)
        return f"Заказ:\n{order_summary}\nВсего: ${self.total_cost():.2f}"

    def __add__(self, other):
        new_order = Order()
        new_order.dishes = self.dishes + other.dishes
        return new_order

    def __gt__(self, other):
        return self.total_cost() > other.total_cost()


# Пример использования:
if __name__ == "__main__":
    order1 = Order()
    order1.add_dish(MainDish("Стейк", 25.00))
    order1.add_dish(Dessert("Чизбургер", 6.50))
    order1.add_dish(Drink("Вино", 10.00, is_alcoholic=True))

    order2 = Order()
    order2.add_dish(MainDish("Салат", 12.00, is_vegetarian=True))
    order2.add_dish(Dessert("Фруктовый салат", 5.00, is_gluten_free=True))

    print(order1)
    print()
    print(order2)

    combined_order = order1 + order2
    print("\nКомбинированный заказ:")
    print(combined_order)

    print(f"Заказ первого гостя стоит дороже чем второго: {order1 > order2}")