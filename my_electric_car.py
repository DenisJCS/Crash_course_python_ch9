from car import Car, ElectricCar

my_beetle = Car('Ford', 'mustang cobra', '1995')
print(my_beetle.get_descriptive_name())

my_zeekr = ElectricCar('zeekr', '001', '2024')
print(my_zeekr.get_descriptive_name())
my_zeekr.battery.describe_battery()
my_zeekr.battery.get_range()


