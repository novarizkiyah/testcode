#An administrator is a special kind of user. 
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) 
# or Exercise 9-5 (page 167). 
# Add an attribute, privileges, that stores a list of strings like "can add post", 
# "can delete post", "can ban user", and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    def describe_user(self):
        print(f"My Data : \nName : {self.first_name} {self.last_name}\nEmail : {self.email}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}, Good Morning!")

#user = User("Nova", "Rizkiyah", "novalailatulrizkiyah@gmail.com")
#user.describe_user()
#user.greet_user()

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = []

    def show_privileges(self):
        print("Privileges : ")
        for privilege in self.privileges:
            print(privilege)

admin = Admin("Nova", "Rizkiyah", "novalailatulrizkiyah@gmail.com")
admin.describe_user()

admin.privileges = ["can add post", "can delete post", "can ban post"]
admin.show_privileges()
