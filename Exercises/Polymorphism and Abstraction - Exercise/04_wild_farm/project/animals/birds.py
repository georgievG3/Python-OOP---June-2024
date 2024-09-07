from typing import List, Type
from project.animals.animal import Bird
from project.food import Food, Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat]

    @property
    def weight_gained(self) -> float:
        return 0.25


class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def allowed_food(self) -> List[Type[Food]]:
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def weight_gained(self) -> float:
        return 0.35
