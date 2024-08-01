#Crash course Python chapter 9
class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        #Added new parameter
        self.odometer_reading = 23 #Set default value
        #Calls def on Car parameter
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
        #Call def ODOMETER
    def read_odometer(self):
        """Print a statment showing curretn odometr millage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        #Updater odo
    def update_odometr(self, millage):
        """Set odometr reading to given value.
           Reject the change if it attepms to roll the odometer back"""
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You cat't roll back an odometer!")
            #Modify ODOMETR addin new on top of old
    def increment_odometer(self, miles):
        """Add the ginven amount to the odometer reading."""
        self.odometer_reading += miles

my_used_car = Car('subary' ,'impreza', '2019')
print(my_used_car.get_descriptive_name())

my_used_car.update_odometr(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_new_car = Car('audi', 'a4', '2024')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometr(5)
my_new_car.read_odometer()





