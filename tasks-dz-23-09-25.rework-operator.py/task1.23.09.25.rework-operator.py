# Виртуальная фабрика роботов-художников
# Вы создаете программное обеспечение для фабрики, которая
# производит роботов-художников. Роботы умеют "рисовать"
# (генерировать строковые паттерны) и их можно комбинировать для
# создания сложных произведений.
# Часть 1:
# Создайте базовый класс PainterBot:
# • Атрибуты: name (имя), style (стиль рисования, например,
# "Пиксельный"), efficiency (эффективность, целое число от 1 до 10).
# • Метод paint(length): возвращает строку, представляющую рисунок
# длиной length. Базовая реализация: возвращает строку из length
# символов #.
# • Создайте два класса-потомка, которые переопределяют метод
# paint:
# • LinePainterBot (рисует линиями): его paint(length) возвращает
# строку из length символов =.
# • WavePainterBot (рисует волнами): его paint(length) возвращает
# строку, где символы ~ и - чередуются (например, для length=5: ~-
# ~-~).
# Часть 2:
# Напишите функцию gallery_exhibition(painter_list, length).
# • Эта функция принимает список роботов-художников (painter_list)
# и длину рисунка length.
# • Функция должна вызвать метод paint(length) у каждого робота в
# списке и напечатать результат вместе с его именем.
# Часть 3:
# Добавьте роботам возможность "объединяться" для совместной
# работы.
# • Перегрузите оператор + (__add__). Когда два робота a и b
# складываются (a + b), должен создаваться и возвращаться новый
# робот (ComboPainterBot).
# • Новый робот получает комбинированное имя: f"Комбо [{a.name} +
# {b.name}]".
# • Его стиль: "Комбинированный".
# • Его эффективность: меньшая из двух эффективностей (слабый
# робот замедляет связку).
# • Его метод paint(length): возвращает строку, где рисунки от двух
# исходных роботов соединены через |. Например, если a.paint(3)
# вернул ###, а b.paint(3) вернул ===, то их комбо вернет ### | ===.


class PainterBot:
    def __init__(self, name, style, efficiency):
        self.name = name
        self.style = style
        self.efficiency = efficiency

    def paint(self, length):
        return "#" * length


class LinePainterBot(PainterBot):
    def __init__(self, name, efficiency):
        super().__init__(name, "Линейный", efficiency)

    def paint(self, length):
        return "=" * length


class WavePainterBot(PainterBot):
    def __init__(self, name, efficiency):
        super().__init__(name, "Волновой", efficiency)

    def paint(self, length):
        return ''.join(['~' if i % 2 == 0 else '-' for i in range(length)])


class ComboPainterBot(PainterBot):
    def __init__(self, painter_a, painter_b):
        name = f"Комбо [{painter_a.name} + {painter_b.name}]"
        style = "Комбинированный"
        efficiency = min(painter_a.efficiency, painter_b.efficiency)
        super().__init__(name, style, efficiency)
        self.painter_a = painter_a
        self.painter_b = painter_b

    def paint(self, length):
        return f"{self.painter_a.paint(length)} | {self.painter_b.paint(length)}"


def __add__(self, other):
    return ComboPainterBot(self, other)

# Применяем перегрузку к классам
PainterBot.__add__ = __add__


def gallery_exhibition(painter_list, length):
    for painter in painter_list:
        print(f"{painter.name}: {painter.paint(length)}")


# Пример использования
if __name__ == "__main__":
    # Создание экземпляров роботов
    bot1 = LinePainterBot(name="Линейный Бот", efficiency=8)
    bot2 = WavePainterBot(name="Волновой Бот", efficiency=5)

    # Выставка
    print("Выставка роботов до объединения:")
    gallery_exhibition([bot1, bot2], 10)

    # Объединение роботов
    combo_bot = bot1 + bot2

    # Выставка комбинированного робота
    print("\nВыставка комбинированного робота:")
    gallery_exhibition([combo_bot], 10)