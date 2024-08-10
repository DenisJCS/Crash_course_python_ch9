from admin import User,Privileges,Admin

new_user = User('denis', 'kelgenbaev', 22, 'florida')
new_user.describe_user()

new_user = Privileges(['Hakkiton 2024' , 'Python developer',' Enterpreneur'])
new_user.show_privileges()
