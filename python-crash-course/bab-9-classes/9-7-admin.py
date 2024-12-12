# An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-5 (page 167). 
# Add an attribute, privileges, that stores a list of strings like "can add post", 
# "can delete post", "can ban user", and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

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
        self.privileges = []
    def show_privileges(self):
        print("Admin privileges: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

user = User("Nova", "Rizkiyah", "n@gmail.com", "twauwag")
user.describe_user()
user.greet_user()

#Make an instance of the User class and call increment_login_attempts() several times. 
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Print the value of login : {user.login_attempts}")

user.reset_login_attempts()
print(f"Print value after reset : {user.login_attempts}")

admin = Admin("Nova", "Rizkiyah", "n@gmail.com", "twauwag")
admin.privileges = ["can add post", "can delete post", "can ban user"]
admin.show_privileges()