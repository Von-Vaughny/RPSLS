class Gesture():
    # Function to initialize variables.
    def __init__(self, name, wins_against):
        self.name = name
        self.wins_against = wins_against
        self.win_count = 0
        self.count = 0

    def __repr__(self):
        return self.name

    def check_vs_opponent(self, opponent):
        if opponent.name in self.wins_against:
            return 1
        else: 
            if opponent.name == self.name:
                return -1
            else: 
                return 0