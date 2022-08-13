from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(10.5, 100)

    def test_init_method_returns_proper_result(self):
        vehicle = Vehicle(10.5, 100)
        self.assertEqual(10.5, vehicle.fuel)
        self.assertEqual(10.5, vehicle.capacity)
        self.assertEqual(100, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.fuel_consumption)

    def test_drive_method_with_correct_data(self):
        self.vehicle.drive(1)
        expected_fuel = 10.5 - 1.25
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_drive_method_with_incorrect_data(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_method_with_correct_data(self):
        self.vehicle.drive(2)
        self.vehicle.refuel(1)
        expected_fuel = 10.5 - 2.5 + 1
        self.assertEqual(expected_fuel, self.vehicle.fuel)

    def test_refuel_method_with_incorrect_data(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_string_method_works_properly(self):
        result_expected = str(self.vehicle)
        self.assertEqual(f"The vehicle has {self.vehicle.horse_power} "
                         f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption",result_expected)


if __name__ == '__main__':
    main()
