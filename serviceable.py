from car import Car

class Serviceable():
    def __init__(self, car : Car):
        self.car = car

    def needs_service(self) -> bool:
        return self.car.engine.needs_service() or self.car.battery.needs_service()