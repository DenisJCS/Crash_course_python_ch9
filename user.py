# 9-3
class User:
    """Attempt crate user"""
    def __init__(self,first_name,last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
    def describe_user(self):
        print(f"User's first name {self.first_name}")
        print(f"User's last name {self.last_name}")
        print(f"Age : {self.age}")
        print(f"Location: {self.location}")
        print(f"Email:{self.email}")
    def greet_user(self):
        print(f"Hello {self.first_name}")
first_user = User('Gon','Fricks',12, 'greed island','gon_hunter@mail.com')
second_user = User('Killua', 'Zoldik', 12, 'greed island', 'killua_ht@mail.com')

first_user.describe_user()
first_user.greet_user()
print("---")

second_user.describe_user()
second_user.greet_user()
print("---")

        