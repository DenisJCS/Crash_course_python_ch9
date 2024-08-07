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
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Printa statment describing the battery size."""
        print(f"This car has a {self.battery_size} - kWH battery.")

    def get_range(self):
        """PRint a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 150:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """
    Initialize attributes of the parent class.
    Then initialize specific to an electric car.
    """
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statment description the battery size"""
        
        print(f"The car has a battery {self.battery_size} - kWh battery")
    def fill_gas_tank(self):
        """Electric car does not have gas tank"""
        print("This car doesn't have gas tank.")


my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())    
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()


