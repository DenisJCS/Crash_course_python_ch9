class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statment showing curretn odometr millage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometr(self, millage):
        """Set odometr reading to given value.
           Reject the change if it attepms to roll the odometer back"""
        if millage >= self.odometer_reading:
            self.odometer_reading = millage
        else:
            print("You cat't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the ginven amount to the odometer reading."""
        self.odometer_reading += miles

#Inheritance
class ElectricCar(Car):
    """
    Initialize attributes of the parent class.
    Then initialize specific to an electric car.
    """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75
    def describe_battery(self):
        """Print a statment description the battery size"""
        print(f"The car has a battery {self.battery_size} - kWh battery")
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())    
my_tesla.describe_battery()
