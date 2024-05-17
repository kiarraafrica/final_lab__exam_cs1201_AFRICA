from utils.dice_game import DiceGame
from utils.user import User

def main_menu():
    usermanager = UserManager()
    while True:
        try:
            print("\nWelcome to Dice Game!")
            print("1. Register")
            print("2. Log-in")
            print("3. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                usermanager.register()
                main_menu()
                break
            elif choice == 2:
                usermanager.login()
                main_menu()
                break
            elif choice == 3:
                print("Exiting...")
                quit()
            else:
                print("Invalid choice. Please try again.")
                continue

        except ValueError:
            print("Invalid choice. Please try again.")

class UserManager:
    def __init__(self):
        self.user = User()

    def register(self):
        self.user.load_users()

        while True:
            self.username = input("\nEnter username: ")
            if self.validate_username():
                break

        while True:
            self.password = input("Enter password: ")
            if self.validate_password():
                self.save_users()
                print("User registered and saved successfully!")
                break
    
    def validate_username(self):
        if len(self.username) < 4:
            print("Username must be atleast 4 characters long.")
            return False
        
        else:
            with open(self.user.user_infos, "r") as file:
                for line in file:
                    if f"{self.username}" in line:
                        print("Username already exists.")
                        return False
            return True
            
    def validate_password(self):
        if len(self.password) < 8:
            print("Password must be atleast 8 characters long.")
            return False
        return True
    
    def save_users(self):
        try:
            with open(self.user.user_infos, "a") as file:
                file.write(f"{self.username}, {self.password}\n")
        except FileNotFoundError:
            return None

    def login(self):
        try:
            self.username = input("\nEnter your username: ")
            self.password = input("Enter your password: ")
            with open(self.user.user_infos, "r") as file:
                for line in file:
                    username, password = line.strip().split(", ")
                    if self.username == username and self.password == password:
                        print("Login successful!")
                        DiceGame.game_menu(self)
                        break
                else:
                    print("Username or password invalid.")
        except FileNotFoundError:
            return None