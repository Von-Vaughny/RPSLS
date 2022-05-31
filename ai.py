from player import Player
import random


class AI(Player):
    # Function to initialize AI player's variables.
    def __init__(self):
        super().__init__()

    # Function to get AI's name.
    def get_name(self, name):
        self.names = name

    # Function to get AI's gesture
    def get_gesture(self):
        self.gesture_no = random.randint(0, 4) 
        self.gesture = self.gestures[self.gesture_no][0]