from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock


class Player():
    # Function to initialize variables.
    def __init__(self):
        self.name = None
        self.is_human = False
        self.turn_wins = 0
        self.round_wins = 0
        self.gestures = {"Rock": Rock(), "Paper": Paper(), "Scissors": Scissors(), "Lizard": Lizard(), "Spock": Spock()}
        self.gesture = None
        self.gesture_no = ""
        self.gestures_list = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
        # self.cur_round_gestures = []
        # self.all_rounds_gestures = []

    # Function to track player gestures each round for def display_log(self).
    # def add_current_gesture(self):
    #     self.cur_round_gestures.append(self.gesture)

    # Function to track player gestures from all rounds for for def display_log(self).
    # def add_round_gesture(self):
    #    self.gesture_list.append(self.current_round_gestures)
    #    self.current_round_gestures.clear()

    # Function to check player's gesture against opponent's gesture. 
    # def check_gesture(self, opponent):
    #    if 
    #    if self.gesture not in self.gestures[int(opponent.gesture_no)][1] and self.gesture != self.gestures[int(opponent.gesture_no)][0]:
    #        self.turn_wins += 1
    #    elif self.gesture in self.gestures[int(opponent.gesture_no)][1]:
    #        opponent.turn_wins += 1

    # Function to get gesture.
    def get_gesture(self):
        return self.gesture

    # Function to set gesture.
    def set_gesture(self, gesture_name):
        self.gesture = self.gestures[gesture_name]

    # Function to add to player's total turn wins.
    def add_turn_win(self):
        self.turn_wins += 1

    # Function to obtain number of player's wins in a round.
    def get_wins(self):
        return self.turn_wins

    # Function to add to player's total wins.
    def add_round_win(self):
        self.round_wins += 1
        
    # Function to obtain player's total wins
    def get_round_wins(self):
        return self.round_wins