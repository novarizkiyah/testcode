# Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
# Write another method called increment_login_attempts() that increments the value of login_attempts by 1. 
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was incremented properly, 
# and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

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
