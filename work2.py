# Задача №2 с использованием полиморфизма.
#
# Продемонстрировать принцип полиморфизма через реализацию разных классов,
# представляющих геометрические формы, и метод для расчёта площади каждой формы.
#
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square),
# каждый из которых переопределяет метод area().
#
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.


class Share():
    def area(self):
        return 0

class Circle(Share):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Share):
    def __init__(self, width, height): # __init__ если нужны переменные
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Share):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side ** 2

def print_area(figure):
    print(figure.area())

circle = Circle(5)
square = Square(7)
print_area(circle)
print_area(square)

# def __init__ пишем в случае если в объекте имеются переменные\характеристики\
# например radius, width, height, side
# если в классе нет переменных\характеристик, то пишем __init__ = None или ни чего не писать!

