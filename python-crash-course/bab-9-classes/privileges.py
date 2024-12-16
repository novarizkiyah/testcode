
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