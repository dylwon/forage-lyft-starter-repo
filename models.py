from datetime import datetime
from datetime import date

from car import Car
from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine
from battery import NubbinBattery
from battery import SpindlerBattery

class Calliope(Car):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int): 
        super().__init__(CapuletEngine(last_service_date, current_mileage, last_service_mileage), SpindlerBattery(datetime.today().date(), last_service_date))
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False



class Glissade(Car):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int): 
        super().__init__(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), SpindlerBattery(datetime.today().date(), last_service_date))
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False



class Palindrome(Car):
    def __init__(self, last_service_date : date, warning_light_on : bool): 
        super().__init__(SternmanEngine(warning_light_on), SpindlerBattery(datetime.today().date(), last_service_date))
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
        


class Rorschach(Car):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int): 
        super().__init__(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage), NubbinBattery(datetime.today().date(), last_service_date))
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False



class Thovex(Car):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int): 
        super().__init__(CapuletEngine(last_service_date, current_mileage, last_service_mileage), NubbinBattery(datetime.today().date(), last_service_date))
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False