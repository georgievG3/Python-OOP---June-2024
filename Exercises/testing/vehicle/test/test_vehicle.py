from project.vehicle import Vehicle

from unittest import TestCase, main

class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(30, 140)

    def test_init(self):
        self.assertEqual(30, self.vehicle.fuel)
        self.assertEqual(30, self.vehicle.capacity)
        self.assertEqual(140, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_without_enough_fuel_raises_exception(self):
        self.assertEqual(30, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(30)


        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(30, self.vehicle.fuel)

    def test_drive_with_enough_fuel(self):
        self.assertEqual(30, self.vehicle.fuel)

        fuel_needed = self.vehicle.fuel_consumption * 20
        left_fuel = self.vehicle.fuel - fuel_needed

        self.vehicle.drive(20)

        self.assertEqual(left_fuel, self.vehicle.fuel)

    def test_refuel_with_no_left_capacity(self):
        self.assertEqual(30, self.vehicle.fuel)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))
        self.assertEqual(30, self.vehicle.fuel)

    def test_refuel_with_enough_capacity(self):
        self.assertEqual(30, self.vehicle.fuel)

        self.vehicle.refuel(0)

        self.assertEqual(30, self.vehicle.fuel)

    def test_string_method(self):
        result = self.vehicle.__str__()

        self.assertEqual("The vehicle has 140 horse power with 30 fuel left and 1.25 fuel consumption", result)


if __name__ == "__main__":
    main()