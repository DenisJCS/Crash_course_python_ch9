class User:
    """Attempt crate user"""
    def __init__(self,first_name,last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    def describe_user(self):
        print(f"User's first name {self.first_name} . User's last name {self.last_name}")
        print(f"User's last name {self.location} . User's age is{self.age}")
    def greet_user(self):
        print(f"Hello {self.first_name}")
    def increment_login_attempts(self):
        """Increment by 1"""
        self.login_attempts += 1
    def reset_logging_attempts(self):
        """Resets attempts to 0"""
        self.login_attempts = 0
user = User('Gon','Fricks',12, 'greed island')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Loging attempts: {user.login_attempts}")

user.reset_logging_attempts()
print(f"Loging attempts (after reset): {user.login_attempts}")


