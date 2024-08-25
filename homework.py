# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).

# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

# 4. Используйте композицию для создания класса `Zoo`,
# который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Animal sound")

    def eat(self):
        print("Animal eat")


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} - Bird sound")


class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} - Mammal sound")


class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} - Reptile sound")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()



class Zoo():
    def __init__(self):
        self.personal = []
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_personal(self, new_personal):
        self.personal.append(new_personal)
        print(f"Добавили {new_personal.name} в зоопарк")





class ZooKeeper():
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        print(f"Животное {animal.name} покормлено")


class Veterinarian():
    def __init__(self, name):
        self.name = name
    def heal_animal(self, animal):
        print(f"Животное {animal} лечено")


bird = Bird("Golub", 5)
mammal1 = Mammal("Cat", 1)
reptile1 = Reptile("Turtle", 10)


animal_sound([bird, mammal1, reptile1])

zoopark = Zoo()
zookeep = ZooKeeper("Alice")
vet = Veterinarian("Jhon")

zoopark.add_animal(bird)
zoopark.add_animal(mammal1)
zoopark.add_animal(reptile1)

zoopark.add_personal(zookeep)
zoopark.add_personal(vet)


animal_sound(zoopark.animals)

zookeep.feed_animal(bird)



