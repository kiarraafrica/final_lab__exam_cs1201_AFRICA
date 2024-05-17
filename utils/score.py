import os

class Score:
    def __init__(self, rankings = "rankings.txt"):
        self.rankings = rankings

    def load_scores(self):
        try:
            if not os.path.exists("rankings"):
                os.makedirs("rankings")
            if not os.path.exists(self.rankings):
                with open(self.rankings, "w"):
                    pass
        except FileNotFoundError:
            return None
