from datetime import date

class Engine():
    def __init__(self):
        pass
        
    def needs_service(self) -> bool:
        pass



class CapuletEngine(Engine):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
    


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on : bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
    


class WilloughbyEngine(Engine):
    def __init__(self, last_service_date : date, current_mileage : int, last_service_mileage : int):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000