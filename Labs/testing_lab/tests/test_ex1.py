# Do not submit in judge
import wave

from Labs.testing_lab.ex_1 import Worker

# All below submit in judge
from unittest import TestCase, main


class TestWorker(TestCase):

    def test_init_worker(self):

        #ACT
        w = Worker("Test", 1000, 100)

        #ASSERT
        self.assertEqual("Test", w.name)
        self.assertEqual(1000, w.salary)
        self.assertEqual(100, w.energy)
        self.assertEqual(0, w.money)

    def test_work_worker_does_not_energy_raises(self):
        #ARRANGE
        w = Worker("Test", 1000, 0)
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        #ACT
        with self.assertRaises(Exception) as ex:
            w.work()

        #ASSERT
        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, w.energy)
        self.assertEqual(0, w.money)

        w = Worker("Test", 1000, -1)

        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(-1, w.energy)
        self.assertEqual(0, w.money)


    def test_work_worker_works(self):

        #Arrange
        w = Worker("Test", 1000, 100)

        self.assertEqual(0, w.money)
        self.assertEqual(100, w.energy)

        #Act
        w.work()

        #Assert
        self.assertEqual(1000, w.money)
        self.assertEqual(99, w.energy)

        # Act
        w.work()

        # Assert
        self.assertEqual(2000, w.money)
        self.assertEqual(98, w.energy)

    def test_rest_worker_energy_increases(self):
        #Arrange
        w = Worker("Test", 1000, 100)
        self.assertEqual(100, w.energy)

        #Act
        w.rest()

        #Assert
        self.assertEqual(101, w.energy)

    def test_get_info(self):

        #Arrange
        w = Worker("Test", 1000, 100)

        #Act
        result = w.get_info()
        expected = 'Test has saved 0 money.'

        #Assert
        self.assertEqual(expected, result)

        #Try with saved money
        w.work()
        # Arrange
        self.assertEqual(w.salary, w.money)

        # Act
        result = w.get_info()
        expected = 'Test has saved 1000 money.'

        # Assert
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
