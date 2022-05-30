class Player():
    # Function to initialize variables.
    def __init__(self):
        self.name = ""
        self.is_human = False
        self.win = False
        self.lose = False
        self.wins = 0
        self.gesture = ""
        self.current_round_gestures = []
        self.gesture_list = []
        self.gestures = ["Rock", "Scissors", "Paper", "Lizard", "Spock"]

    # Function to track player's gesture
    def add_current_gesture(self):
        self.current_round_gestures.append(self.gesture)

    # Function to get number of player's wins
    def get_wins(self):
        return self.wins

    # Function to add to player's wins.
    def add_win(self):
        self.wins += 1