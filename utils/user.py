import os

class User:
    def __init__(self, user_infos = "users.txt"):
        self.user_infos = user_infos

    def load_users(self):
        try:
            if not os.path.exists("users"):
                os.makedirs("users")
            if not os.path.exists(self.user_infos):
                with open(self.user_infos, "w"):
                    pass
        except FileNotFoundError:
            return None