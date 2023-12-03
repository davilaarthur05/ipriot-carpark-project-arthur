from sensor import Sensor
from display import Display
from pathlib import Path
from datetime import datetime
import json


class CarPark:
    def __init__(self, location, capacity, log_file="log_file.txt", plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = Path(log_file)
        if not self.log_file.exists():
            self.log_file.touch()

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def __str__(self):
        return f"Welcome to {self.location} Car Park!!"

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def _log_car(self, action, plate):
        with self.log_file.open(mode="a") as file:
            file.write(f"{plate} {action} on the {datetime.now().strftime('%d-%m %H:%M')}\n")

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car("entered", plate)

    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car("exited", plate)

    def update_displays(self, entry=True):
        for display in self.displays:
            display.update({"Bays": self.available_bays, "Temperature": 42})

    def write_config(self):
        with open("config.json", "w") as file:
            json.dump({"location": self.location,
                       "capacity": self.capacity,
                       "log_file": str(self.log_file)}, file)

    @staticmethod
    def from_config(config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return CarPark(config["location"], config["capacity"], log_file=config["log_file"])
