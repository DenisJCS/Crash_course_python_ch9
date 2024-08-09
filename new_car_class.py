from car import Car

my_new_car = Car('porsche', '911', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 50
my_new_car.read_odometer()

from car import ElectricCar

my_tesla = ElectricCar('tesla','model y', 2024)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
