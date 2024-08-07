class Restaurant:
    """A simple attempt to restaurant"""
    def __init__(self,restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
    def describe_restaurant(self):
        """Print these two pieces of inforamtion"""
        print(f"The restaurant name is {self.restaurant_name}!")
        print(f"Cusine is {self.cusine_type}!")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """A simple ice cream stand (inheiting from restaurant class)."""
    def __init__(self,restaurant_name, cusine_type, flavors):
        """Initialize ice cream stand (inheriting from restaurant class)."""
        super().__init__(restaurant_name, cusine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Display ice cream flavor."""
        print(f"The flavor are:")
        for flavor in self.flavors:
            print(f"-{flavor}")

ice_cream = IceCreamStand('ice cream flavor', 'ice cream', ['chocolate','vanilla', 'banana'])
ice_cream.display_flavors()


#Output
The flavor are:
-chocolate
-vanilla
-banana
