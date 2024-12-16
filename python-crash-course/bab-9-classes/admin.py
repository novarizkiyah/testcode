from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self, first_name, last_name, email, passwords):
        super().__init__(first_name, last_name, email, passwords)
        self.privileges_manager = Privileges()