from datetime import date

class Battery():
    def __init__(self, current_date : date, last_service_date : date): 
        self.current_date = current_date
        self.last_service_date = last_service_date
    def needs_service(self) -> bool:
        pass



class NubbinBattery(Battery): 
    def __init__(self, current_date : date, last_service_date : date):
        super().__init__(current_date, last_service_date)

    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_date.year > 4
    


class SpindlerBattery(Battery): 
    def __init__(self, current_date : date, last_service_date : date):
        super().__init__(current_date, last_service_date)

    def needs_service(self) -> bool:
        return self.current_date.year - self.last_service_date.year > 2