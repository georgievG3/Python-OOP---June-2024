from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return "Meow"


class Dog(Animal):

    def make_sound(self):
        return "Bark"


class Turtle(Animal):

    def make_sound(self):
        return "Turtle Sound"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog("Sharo"), Cat("Kitty"), Turtle("bob")]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
