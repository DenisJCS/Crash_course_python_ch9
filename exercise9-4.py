#Using new knowledge from chapter 9 on program restaurant.
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
    def rest_num(self):
        """Print number of customers that restaurant served"""
        print(f"\nThis is number of customers {self.number_served}")
    def update_number(self,customer):
        """Set programm read new entered values"""
        self.number_served = customer
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")



frenc_restaurant = Restaurant("Madlen","French/British")
greek_restaurant = Restaurant("Appolonia","Meditaruian-Greek")
asian_restaurant = Restaurant("Faiza","Central Asia Kitchen")

frenc_restaurant.describe_restaurant()
frenc_restaurant.number_served = 23 #Specify def name
frenc_restaurant.rest_num() #Call def saved function
greek_restaurant.update_number(43)




greek_restaurant.describe_restaurant()
print("---")
greek_restaurant.update_number(100) #Updated value 
greek_restaurant.rest_num() #Call saved function





