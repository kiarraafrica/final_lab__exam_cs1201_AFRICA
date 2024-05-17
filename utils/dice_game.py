import random
import datetime
from utils.score import Score

class DiceGame:
    def __init__(self, username):
        self.username = username
        self.score = Score()

    def game_menu(self):
        dicegame = DiceGame(self.username)
        while True:
            try:
                print("\nWelcome to Game Menu!")
                print("1. Play Game")
                print("2. Show Top Scores")
                print("3. Log Out")

                choice = int(input("Enter your choice: "))
                if choice == 1:
                    dicegame.play_game()
                    break
                elif choice == 2:
                    dicegame.show_top_scores()
                    break
                elif choice == 3:
                    print("Logging out... User logged out successfully!")
                    return False
                else:
                    print("Invalid choice. Please try again.")
                    break
            
            except ValueError:
                print("Invalid choice. Please try again.")

    def play_game(self):
        print(f"Starting game as {self.username}\n")

        self.user_score = 0
        self.cpu_score = 0
        self.stage = 1
        self.stages_won = 0 

        while True:
            self.round = 1
            self.user_point = 0
            self.cpu_point = 0

            print("Dice rolling...\n")

            while self.round <= 3:
                user_dice = random.randint(1, 6)
                cpu_dice = random.randint(1, 6) 

                print(f"{self.username} rolled: {user_dice}")
                print(f"CPU rolled: {cpu_dice}")   
                if user_dice > cpu_dice:
                    print(f"---{self.username} win this round.")
                    self.user_point += 1
                elif user_dice < cpu_dice:
                    print("---CPU win this round.")
                    self.cpu_point += 1
                else:
                    print("*It's a tie*")


                self.round += 1

            while self.user_point == self.cpu_point:
                print("\nTie break round!")
                user_dice = random.randint(1, 6)
                cpu_dice = random.randint(1, 6) 

                print(f"{self.username} rolled: {user_dice}")
                print(f"CPU rolled: {cpu_dice}")   
                if user_dice > cpu_dice:
                    print(f"---{self.username} win this round.")
                    self.user_point += 1
                elif user_dice < cpu_dice:
                    print("---CPU win this round.")
                    self.cpu_point += 1
                    break

            if self.user_point > self.cpu_point:
                print(f"\n{self.username} won this stage.")
                self.user_score += self.user_point + 3
                self.stages_won += 1

                print(f"Total Points: {self.user_score} | Stage/s Won: {self.stages_won}")

                choice = input("\nDo you wish to (1) continue to next stage or (2) quit the game?: ")
                if choice == '1':
                    self.stage += 1
                elif choice == '2':
                    print(f"Game over. You won {self.stages_won} with a total point sof {self.user_score}")
                    self.save_scores()
                    self.game_menu()
                    break

            elif self.user_point < self.cpu_point:
                print(f"\nYou lost this stage, {self.username}. It's game over.")
                self.save_scores()
                self.game_menu()
                break

    def save_scores(self):
        self.score.load_scores()

        date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.score.rankings, "a") as file:
                file.write(f"{date_time} / {self.username}: \tScore - {self.user_score}, \tWins - {self.stages_won}\n")
        except Exception as e:
            print(f"Error saving... {e}")
            
    def show_top_scores(self):
        try:
            with open(self.score.rankings, "r") as file:
                lines = file.readlines()

            if not lines:
                print("\nNo games played yet. Play a game to see top scores.")
                return
            
            rankings = []
            for line in lines:
                parts = line.strip().split(" / ")
                date_time = parts[0].strip()
                date_time_1 = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
                username_2 = parts[1]. split(": ")
                username = username_2[0].strip()
                user_score_2 = username_2[1].split(", ")
                user_score = int(user_score_2[0].split(" - ")[1].strip())
                stages_won = int(user_score_2[1].split(" - ")[1].strip())

                rankings.append((date_time_1, username, user_score, stages_won))

            rankings.sort(key=lambda x: x[2], reverse=True)

            print("\n\t\t\t----TOP SCORES----")
            print("Rank\tDate&Time\t\tPlayer\t\tScores\t\tWins")
            for rank, (date_time_1, username, user_score, stages_won) in enumerate(rankings[:10], 1):
                print(f"{rank}\t{date_time_1}\t{username}\t\t{user_score}\t\t{stages_won}")
        
        except FileNotFoundError:
            print("\nNo games played yet. Play a game to see top scores.")
            self.game_menu()