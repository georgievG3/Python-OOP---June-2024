from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Test", 10, 100, 20)


    def test_init(self):
        self.assertEqual("Test", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battle_same_username(self):
        enemy = Hero("Test", 10, 100, 20)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_fighting_with_negative_health(self):
        enemy = Hero("Test1", 5, 100, 10)
        self.hero.health = -1

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fighting_with_zero_health(self):
        enemy = Hero("Test1", 5, 100, 10)
        self.hero.health = 0

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_enemy_hero_fighting_with_zero_health(self):
        enemy = Hero("Test1", 5, 0, 10)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight Test1. He needs to rest", str(ex.exception))

    def test_enemy_hero_fighting_with_negative_health(self):
        enemy = Hero("Test1", 5, -1, 10)

        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)

        self.assertEqual("You cannot fight Test1. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy = Hero("Test1", 10, 100, 20)

        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, enemy.health)

        result = self.hero.battle(enemy)

        self.assertEqual(-100, self.hero.health)
        self.assertEqual(-100, enemy.health)

        self.assertEqual("Draw", result)

    def test_enemy_hero_loses(self):
        enemy = Hero("Test1", 1, 100, 20)

        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, enemy.health)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(20, self.hero.damage)

        result = self.hero.battle(enemy)

        self.assertEqual(11, self.hero.level)
        self.assertEqual(85, self.hero.health)
        self.assertEqual(25, self.hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_hero_wins(self):
        enemy = Hero("Test1", 10, 100, 11)
        self.hero.level = 1

        result = self.hero.battle(enemy)

        self.assertEqual(11, enemy.level)
        self.assertEqual(85, enemy.health)
        self.assertEqual(16, enemy.damage)
        self.assertEqual("You lose", result)

    def test_string_method(self):

        result = self.hero.__str__()

        self.assertEqual("Hero Test: 10 lvl\nHealth: 100\nDamage: 20\n", result)



if __name__ == "__main__":
    main()