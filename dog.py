class Dog:
    """A simmple attemp to model a dog"""
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def rollover(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} to rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Luci', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My do is {my_dog.age} years old.")
my_dog.sit()
my_dog.rollover()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {my_dog.age} years old.")
your_dog.sit()
your_dog.rollover()
