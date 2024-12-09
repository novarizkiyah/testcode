# Make a class called User. Create two attributes called first_name and last_name, 
# and then create several other attributes that are typically stored in a user profile. 
# Make a method called describe_user() that prints a summary of the user’s information. 
# Make another method called greet_user() that prints a personalized greeting to the user.

# Create several instances representing different users, and call both methods for each user.

class User:
    def __init__(self, first_name, last_name, email, passwords):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwords = passwords
    def describe_user(self):
        print(f"First Name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Passwords : {self.passwords}")
    def greet_user(self):
        print(f"Hallo, {self.first_name} {self.last_name} Welcome in this site! Have a nice day!")

user1 = User("Nova", "Rizkiyah", "n@gmail.com", "twauwag")
user2 = User("Ratmi", "Mawar", "t@gmail.com", "jdahjadjahd")
user3 = User("Melati", "Pelangi", "y@gmail.com", "sasanjaa")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

