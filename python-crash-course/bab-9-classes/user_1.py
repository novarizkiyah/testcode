from user import User

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