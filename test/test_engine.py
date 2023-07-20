import unittest
from datetime import datetime

from engine.engine_types.capulet_engine import CapuletEngine
from engine.engine_types.sternman_engine import SternmanEngine
from engine.engine_types.willoughby_engine import WilloughbyEngine

class TestCappuletEngine(unittest.TestCase):
    def test_cappulet_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 40000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
    
    def test_cappulet_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 20000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service()) 
    
class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())
