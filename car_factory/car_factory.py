from car import car

from engine.engine_types.capulet_engine import CapuletEngine
from engine.engine_types.sternman_engine import SternmanEngine
from engine.engine_types.willoughby_engine import WilloughbyEngine

from battery.battery_types.nubbin_battery import NubbinBattery
from battery.battery_types.spindler_battery import SpindlerBattery

from tires.tire_types.carrigan_tire import CarriganTire
from tires.tire_types.octoprime_tire import OctoprimeTire

class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tires_array)
        new_car = car(engine, battery, tires)
        return new_car 
    
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_array):
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = OctoprimeTire(tires_array)
        new_car = car(engine, battery, tires)
        return new_car 
    
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tires_array):
        engine = SternmanEngine(last_service_date, current_mileage, last_service_date)
        battery = SpindlerBattery(current_date, last_service_date)
        tires = CarriganTire(tires_array)
        new_car = car(engine, battery, tires)
        return new_car 
    
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        tires = OctoprimeTire(tires_array)
        new_car = car(engine, battery, tires)
        return new_car 
    
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tires_array):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_date)
        battery = NubbinBattery(current_date, last_service_date)
        tires = CarriganTire(tires_array)
        new_car = car(engine, battery, tires)
        return new_car 