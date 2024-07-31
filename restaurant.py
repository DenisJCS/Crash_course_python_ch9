#Exerxise 9-1/9-2 chapter 9
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

frenc_restaurant = Restaurant("Madlen","French/British")
greek_restaurant = Restaurant("Appolonia","Meditaruian-Greek")
asian_restaurant = Restaurant("Faiza","Central Asia Kitchen")

frenc_restaurant.describe_restaurant()
print("---")

greek_restaurant.describe_restaurant()
print("---")

asian_restaurant.describe_restaurant()
print("---")

