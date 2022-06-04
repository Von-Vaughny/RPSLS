from player import Player
from getpass import getpass
import re


class Human(Player):
    # Function to initialize human player's variables.
    def __init__(self):
        super().__init__()
        self.is_human = True
        
    # Function to obtain player's name.
    def get_name(self, players, reserved_names):
        players_names = []
        if len(players):
            for player in players:
                if player.name not in reserved_names:
                    players_names.append(player.name)
        while not(self.name):
            self.name = re.sub(r"[^a-zA-Z]", "", input("\nWhat is your name player? ")).title()
            if self.name in reserved_names + players_names:
                print(f"Cannot select any of the following names:", '%s' % ', '.join(map(str, reserved_names + players_names))) 
                self.name = "" 
            elif self.name:
                self.sure = ""
                while len(self.sure) != 1:
                    self.sure = re.sub(r"[^0-1]", "", input(f"Are you sure you want to be named {self.name}? (Input 0 for no, 1 for yes): "))
                    if int(self.sure) == 0:
                        self.name = ""

    # Function to obtain player's gesture
    def get_gesture(self):
        self.gesture_no = ""
        while len(self.gesture_no) != 1:
            print(f"\n{self.name} select a gesture: ")
            for i, gesture in enumerate(self.gestures):
                print(f"Input {i+1} for {gesture[0]}")
            self.gesture_no = re.sub(r"[^1-5]", "", getpass(f"\n{self.name} selects gesture: "))
        self.gesture_no = int(self.gesture_no) - 1
        self.gesture = self.gestures[self.gesture_no][0]