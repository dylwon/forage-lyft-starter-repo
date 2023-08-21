from datetime import date

class Tire():
    def __init__(self, lst : []):
        self.wear = lst
        for tire_wear in self.wear:
            if tire_wear < 0 or tire_wear > 1:
                
                exit()

class CarriganTire(Tire):
    def __init__(self, lst : []):
        super().__init__(lst)

    def needs_service(self) -> bool:
        for tire_wear in self.wear:
            if tire_wear >= 0.9:
                return True
        return False

class OctoprimeTire(Tire):
    def __init__(self, lst : []):
        super().__init__(lst)

    def needs_service(self) -> bool:
        total_wear = 0
        for tire_wear in self.wear:
            total_wear += tire_wear
        return True if total_wear >= 3 else False