from datetime import datetime
from datetime import date
from car import Car
from engine import Engine
from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine
from battery import Battery
from battery import NubbinBattery
from battery import SpindlerBattery

class CarFactory(Car):
    def __init__(self, engine : Engine, battery : Battery):
        super().__init__(engine, battery)
        self.current_mileage = engine.current_mileage
        self.last_service_mileage = engine.last_service_mileage
        self.current_date = battery.current_date
        self.last_service_date = battery.last_service_date

    def create_calliope(self, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(CapuletEngine(last_service_date, current_mileage, last_service_mileage), SpindlerBattery(datetime.today().date(), last_service_date))

    def create_glissade(self, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), SpindlerBattery(datetime.today().date(), last_service_date))

    def create_palindrome(self, last_service_date : date, warning_light_on : bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(datetime.today().date(), last_service_date))

    def create_rorschach(self, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), NubbinBattery(datetime.today().date(), last_service_date))

    def create_thovex(self, last_service_date : date, current_mileage : int, last_service_mileage : int) -> Car:
        return Car(CapuletEngine(last_service_date, current_mileage, last_service_mileage), NubbinBattery(datetime.today().date(), last_service_date))

