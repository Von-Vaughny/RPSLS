from player import Player
from getpass import getpass
import re


class Human(Player):
    # Function to initialize human player's variables.
    def __init__(self):
        super().__init__(self)
        self.is_human = True
        
    # Function to get player's name.
    def get_name(self):
        while not(self.name):
            self.name = re.sub(r"[^a-zA-Z]", "", input("\nWhat is your name player? "))

    # Function to get player's gesture
    def get_gesture(self):
        self.gesture_no = ""
        while not self.gesture_no:
            print("\nSelect a gesture: ")
            for i, gesture in enumerate(self.gestures):
                print(f"Input {i+1} for {gesture[0]}")
            self.gesture_no = re.sub(r"[^1-6]", "", getpass("\nSelect a gesture: "))
        return int(self.gesture_no) - 1
