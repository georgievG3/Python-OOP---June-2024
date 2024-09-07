from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):

    @staticmethod
    def make_sound():
        return "Squeak"

    @property
    def allowed_food(self):
        return [Vegetable, Fruit]

    @property
    def weight_gained(self) -> float:
        return 0.10


class Dog(Mammal):

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_gained(self) -> float:
        return 0.40


class Cat(Mammal):

    @staticmethod
    def make_sound():
        return "Meow"

    @property
    def allowed_food(self):
        return [Meat, Vegetable]

    @property
    def weight_gained(self) -> float:
        return 0.30


class Tiger(Mammal):

    @staticmethod
    def make_sound():
        return "ROAR!!!"

    @property
    def allowed_food(self):
        return [Meat]

    @property
    def weight_gained(self) -> float:
        return 1.00
