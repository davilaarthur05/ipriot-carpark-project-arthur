from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

car_park = CarPark.from_config('moondalup.txt')
entry_sensor = EntrySensor(1, car_park, is_active=True)
exit_sensor = ExitSensor(2, car_park, is_active=True)
display = Display(1, car_park, message="Welcome to Moondalup", is_on=True)

car_park.register(entry_sensor)
car_park.register(exit_sensor)
car_park.register(display)

entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()
entry_sensor.detect_vehicle()

exit_sensor.detect_vehicle()
exit_sensor.detect_vehicle()
