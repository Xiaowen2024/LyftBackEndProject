import unittest
from datetime import datetime

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())