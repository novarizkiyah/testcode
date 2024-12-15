from user import User
from user_1 import Admin, Privileges

user = User("Nova", "Rizkiyah", "n@gmail.com", "twauwag")
user.describe_user()
user.greet_user()

#Make an instance of the User class and call increment_login_attempts() several times. 
for x in range (6):
    user.increment_login_attempts()
print(f"Print the value of login : {user.login_attempts}")

user.reset_login_attempts()
print(f"Print value after reset : {user.login_attempts}")

admin = Admin("Nova", "Rizkiyah", "n@gmail.com", "twauwag")

admin.privileges_manager.show_privileges()

admin.privileges_manager.privileges_list = ["can add post", "can delete post", "can ban user"]
admin.privileges_manager.show_privileges()