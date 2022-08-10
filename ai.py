from player import Player
import random


class AI(Player):
    # Function to initialize AI player's variables.
    def __init__(self, name):
        super().__init__()
        self.name = name

    # Function to obtain AI's gesture
    def select_gesture(self):
        self.gesture_no = random.randint(0, 4) 
        self.set_gesture(self.gestures_list[self.gesture_no])