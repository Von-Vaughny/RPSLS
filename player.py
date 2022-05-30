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
        self.gestures = [["Rock", [], []], 
                         ["Scissors", [], []], 
                         ["Paper", [], []], 
                         ["Lizard"], [], [], 
                         ["Spock", [], []]]

    # Function to track player gestures each round.
    def add_current_gesture(self):
        self.current_round_gestures.append(self.gesture)

    # Function to track player gestures from all rounds.
    def add_round_gesture(self):
        self.gesture_list.append(self.current_round_gestures)
        self.current_round_gestures.clear()

    # Function to get number of player's wins
    def get_wins(self):
        return self.wins

    # Function to add to player's wins.
    def add_win(self):
        self.wins += 1