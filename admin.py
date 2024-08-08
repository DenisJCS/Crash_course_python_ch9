
class User:
    """Attempt crate user"""
    def __init__(self,first_name,last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"User's first name {self.first_name}")
        print(f"User's last name {self.last_name}")
        print(f"Age : {self.age}")
        print(f"Location: {self.location}")
    def greet_user(self):
        print(f"Hello {self.first_name}")
    


class Admin(User):
    """A simple class name"""
    def __init__(self, first_name, last_name, age, location, privileges):
        super().__init__(first_name, last_name, age, location)
        self.privileges = privileges

    def show_privileges(self):
        """Display privileges"""
        print("Privileges")
        for privileg in self.privileges:
            print(f"-{privileg}")
        
user_info = Admin('Denis', 'Kelgenbaev', 22, 'Florida' , ['python developer', 'enterpreneur', 'shark'])
user_info.show_privileges()
