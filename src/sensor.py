import random
from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(self, id, car_park, is_active=False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def _scan_plate(self):
        return "FAKE-" + format(random.randint(0, 999), "03d")

    def __str__(self):
        return f"{self.id}: Sensor {'is active' if self.is_active else 'is not active'}"

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)

    def _scan_plate(self):
        return random.choice(self.car_park.plates)
