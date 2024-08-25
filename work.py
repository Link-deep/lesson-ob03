
# Создайте класс Animal с методом make_sound().
# Затем создайте несколько дочерних классов (например, Dog, Cat, Cow),
# которые наследуют Animal, но изменяют его поведение (метод make_sound()).
#
# В конце создайте список содержащий экземпляры этих животных и вызовите make_sound()
# для каждого животного в цикле.


class Animal():
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Gav")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Cow(Animal):
    def make_sound(self):
        print("Moo")



animals = [Animal(), Dog(), Cat(), Cow()]
for animal in animals:
    animal.make_sound()



