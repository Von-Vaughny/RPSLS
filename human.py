from player import Player
from getpass import getpass
import re


class Human(Player):
    # Function to initialize human player's variables.
    def __init__(self, players_list):
        super().__init__()
        self.is_human = True
        self.players_list = [player for player in players_list]
        self.player_reserved_names = ["Siri", "Alexa", "Bixby"]
        
    # Function to obtain player's name.
    def get_name(self):
        self.players_names = []
        if len(self.players_list):
            for i, player in enumerate(self.players_list):
                if player.name not in self.player_reserved_names:
                    self.players_names.append(self.players_list[i].name)
        while not(self.name):
            self.name = re.sub(r"[^a-zA-Z]", "", input("\nWhat is your name player? "))
            if self.name in self.player_reserved_names or self.name in self.players_names:
                print(f"Cannot select any of the following names:", '%s' % ', '.join(map(str, self.player_reserved_names + self.players_names))) 
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
            self.gesture_no = re.sub(r"[^1-6]", "", getpass(f"\n{self.name} selects a gesture: "))
        self.gesture_no = int(self.gesture_no) - 1
        self.gesture = self.gestures[self.gesture_no][0]