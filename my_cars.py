import car

my_mustang = car.Car('Ford', 'mustand cobra', 2024)
print(my_mustang.get_descriptive_name())

my_zeekr = car.ElectricCar('Zeekr', '001', 2024)
print(my_zeekr.get_descriptive_name())

from car import ElectricCar as EC



my_zeekr = EC('Zeekr', '002', 2024)
print(my_zeekr.get_descriptive_name())
