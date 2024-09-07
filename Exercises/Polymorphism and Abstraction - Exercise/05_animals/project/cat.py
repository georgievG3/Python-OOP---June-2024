from project.animal import Animal


class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound():
        return "Meow meow!"

