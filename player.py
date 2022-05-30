class Player():
    # Function to initialize variables.
    def __init__(self):
        self.name = ""
        self.is_human = False
        self.win = False
        self.lose = False
        self.wins = 0
        self.gesture_no = ""
        self.gesture = ""
        self.current_round_gestures = []
        self.gesture_list = []
        # [Gesture, [Wins Against]]
        self.gestures = [["Rock", ["Scissors", "Lizard"]], 
                         ["Scissors", ["Paper", "Lizard"]], 
                         ["Paper", ["Rock", "Spock"]], 
                         ["Lizard", ["Paper", "Spock"]], 
                         ["Spock", ["Scissors", "Rock"]]]

    # Function to track player gestures each round for def display_log(self).
    # def add_current_gesture(self):
    #     self.current_round_gestures.append(self.gesture)

    # Function to track player gestures from all rounds for for def display_log(self).
    # def add_round_gesture(self):
    #    self.gesture_list.append(self.current_round_gestures)
    #    self.current_round_gestures.clear()

    # Function to check player gesture against opponent gesture. 
    def check_gesture(self, opponent):
        if int(self.gesture_no) == int(opponent.gesture_no):
            self.win = True
            opponent.win = True
        elif self.gestures[int(self.gesture_no)][0] in self.gestures[int(opponent.gesture_no)][1]:
            self.lose = True
            opponent.win = True
        else:
            self.win = True
            opponent.lose = True

    # Function to get number of player's wins
    def get_wins(self):
        return self.wins

    # Function to add to player's wins.
    def add_win(self):
        self.wins += 1
        
