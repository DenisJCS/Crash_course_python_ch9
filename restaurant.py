class Restaurant:
    """A simple attempt to restaurant"""
    def __init__(self,restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
    def describe_restaurant(self):
        """Print these two pieces of inforamtion"""
        print(f"The restaurant name is {self.restaurant_name}!")
        print(f"Cusine is {self.cusine_type}!")
    def set_number_served(self, guests):
        """Print number of served guests"""
        self.number_served = guests
    def increment_number_served(self, increment):
        """Increment number of guest been served"""
        self.number_served += increment

restaurant = Restaurant('french' ,'european')
print(f"Restaurant server: {restaurant.number_served}")

restaurant.number_served = 150
print(f"Restaurant server: {restaurant.number_served}")

restaurant.number_served = 300
print(f"Restaurant server: {restaurant.number_served}")

restaurant.increment_number_served(150)
print(f"Number server: {restaurant.number_served}")















