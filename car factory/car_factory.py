from car import car

from engine.engine_types.capulet_engine import CapuletEngine
from engine.engine_types.sternman_engine import SternmanEngine
from engine.engine_types.willoughby_engine import WilloughbyEngine

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery

class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = car(engine, battery)
        return new_car 
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = car(engine, battery)
        return new_car 
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        new_car = car(engine, battery)
        return new_car 
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        new_car = car(engine, battery)
        return new_car 
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        new_car = car(engine, battery)
        return new_car 