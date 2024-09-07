from project.mammal import Mammal

from unittest import TestCase, main

class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal("Test", "monkey", "monkey sound")

    def test_init(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("monkey", self.mammal.type)
        self.assertEqual("monkey sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_returns_string(self):

        result = self.mammal.make_sound()

        self.assertEqual(f"Test makes monkey sound", result)

    def test_get_kingdom_returns_animals(self):

        result = self.mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info(self):

        result = self.mammal.info()

        self.assertEqual(f"Test is of type monkey", result)

if __name__ == "__main__":
    main()