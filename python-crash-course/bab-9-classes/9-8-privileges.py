#Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show its privileges.

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def describe_user(self):
        print(f"My Data : \nName : {self.first_name} {self.last_name}\nEmail : {self.email}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Good Morning!")

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        # inisiasi sebuah instance dari privileges class dengan empty list 
        self.privileges_manager = PrivilegesManager()

class PrivilegesManager:
    def __init__(self, privileges_list=[]):
        self.privileges_list = privileges_list

    def show_privileges(self):
        print("Privileges : ")
        if self.privileges_list:
            for privilege in self.privileges_list:
                print(f" - {privilege}")
        else:
            print(f" - This user has no privileges")

priv = Admin("Nova", "Rizkiyah", "n@gmail.com")
priv.describe_user()
priv.greet_user()

priv.privileges_manager.show_privileges()

print(f"Adding privileges:")
admin_privileges = ["can add post", "can delete post", "can ban post"]

priv.privileges_manager.privileges_list = admin_privileges
priv.privileges_manager.show_privileges()