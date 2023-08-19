from abc import ABC, abstractmethod
import engine
import battery

class Car(ABC):
    def __init__(self, engine : engine, battery : battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
    
