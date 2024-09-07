from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):

    def setUp(self) -> None:

        self.player = SoccerPlayer("TestName", 18, 5, "Barcelona")

    def test_init_method(self):

        self.assertIsInstance(self.player.name, str)
        self.assertIsInstance(self.player.age, int)
        self.assertIsInstance(self.player.goals, int)
        self.assertIsInstance(self.player.team, str)
        self.assertIsInstance(self.player.achievements, dict)

        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_name_setter(self):

        self.assertEqual("TestName", self.player.name)

        with self.assertRaises(ValueError) as error:
            self.player.name = "err"

        self.assertEqual("Name should be more than 5 symbols!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.player.name = "error"

        self.assertEqual("Name should be more than 5 symbols!", str(error.exception))

        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_age_setter(self):

        self.assertEqual(18, self.player.age)

        with self.assertRaises(ValueError) as error:
            self.player.age = 15

        self.assertEqual("Players must be at least 16 years of age!", str(error.exception))
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_goals_setter(self):

        self.assertEqual(5, self.player.goals)

        self.player.goals = -1
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(0, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_team_setter(self):

        self.assertEqual("Barcelona", self.player.team)

        with self.assertRaises(ValueError) as error:
            self.player.team = "Error"

        self.assertEqual(f"Team must be one of the following: {', '.join(self.player._VALID_TEAMS)}!", str(error.exception))
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_change_team_with_invalid_new_team(self):

        self.assertEqual("Barcelona", self.player.team)

        result = self.player.change_team("No_Team")

        self.assertEqual("Invalid team name!", result)
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_change_team_with_valid_new_team(self):

        self.assertEqual("Barcelona", self.player.team)

        result = self.player.change_team("PSG")

        self.assertEqual("Team successfully changed!", result)
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("PSG", self.player.team)
        self.assertEqual({}, self.player.achievements)

    def test_add_new_achievement(self):

        self.assertEqual({}, self.player.achievements)

        result = self.player.add_new_achievement("Test_Achievement")

        self.assertEqual(f"{'Test_Achievement'} has been successfully added to the achievements collection!", result)
        self.assertEqual({"Test_Achievement": 1}, self.player.achievements)

        result = self.player.add_new_achievement("Test_Achievement")

        self.assertEqual(f"{'Test_Achievement'} has been successfully added to the achievements collection!", result)
        self.assertEqual({"Test_Achievement": 2}, self.player.achievements)
        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)

    def test_lt_method(self):
        other = SoccerPlayer("OtherName", 17, 10, "Real Madrid")

        result = self.player.__lt__(other)
        self.assertEqual(f"{other.name} is a top goal scorer! S/he scored more than {self.player.name}.", result)

        other.goals = 1
        result = self.player.__lt__(other)
        self.assertEqual(f"{self.player.name} is a better goal scorer than {other.name}.", result)

        self.assertEqual("TestName", self.player.name)
        self.assertEqual(18, self.player.age)
        self.assertEqual(5, self.player.goals)
        self.assertEqual("Barcelona", self.player.team)
        self.assertEqual({}, self.player.achievements)

if __name__ == "__main__":
    main()