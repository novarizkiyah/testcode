# Start with your work from Exercise 9-8 (page 178). Store the classes User, 
# Privileges and Admin in one module. Create a separate file, 
# make an Admin instance, 
# and call show_priveleges() to show that everything is working correctly.

class User:
    def __init__(self, first_name, last_name, email, passwords):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwords = passwords
        self.login_attempts = 0
    def describe_user(self):
        print(f"First Name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Passwords : {self.passwords}")
    def greet_user(self):
        print(f"Hallo, {self.first_name} {self.last_name} Welcome in this site! Have a nice day!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
class Admin(User):
    def __init__(self, first_name, last_name, email, passwords):
        super().__init__(first_name, last_name, email, passwords)
        self.privileges_manager = Privileges()
class Privileges:
    def __init__(self):
        self.privileges_list = []
    def show_privileges(self):
        print("Admin privileges: ")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f"- {privilege}")
        else:
            print("This user has no privileges")

user = User("Nova", "Rizkiyah", "n@gmail.com", "twauwag")
user.describe_user()
user.greet_user()

#Make an instance of the User class and call increment_login_attempts() several times. 
for x in range(6):
    user.increment_login_attempts()

print(f"Print the value of login : {user.login_attempts}")

user.reset_login_attempts()
print(f"Print value after reset : {user.login_attempts}")

admin = Admin("Nova", "Rizkiyah", "n@gmail.com", "twauwag")

admin.privileges_manager.show_privileges()

admin.privileges_manager.privileges_list = ["can add post", "can delete post", "can ban user"]
admin.privileges_manager.show_privileges()