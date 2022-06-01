class Player():
    # Function to initialize variables.
    def __init__(self):
        self.name = ""
        self.is_human = False
        self.wins = float(0)
        self.total_wins = 0
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
        if self.gesture_no == opponent.gesture_no:
            self.wins += float(0.5)
            opponent.wins += float(0.5)
        elif self.gesture in self.gestures[int(opponent.gesture_no)][1]:
            opponent.wins += 1
        elif self.gestures not in self.gestures[int(opponent.gesture_no)][1]:
            self.wins += 1

    # Function to obtain number of player's wins in a round.
    def get_wins(self):
        return self.wins

    # Function to add to player's total wins.
    def add_total_win(self):
        self.total_wins += 1
        
    # Function to obtain player's total wins
    def get_total_wins(self):
        return self.total_wins
