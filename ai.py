from player import Player
import random


class AI(Player):
    # Function to initialize AI player's variables.
    def __init__(self):
        super().__init__(self)

    # Function to get AI's name.
    def name_AI(self, AI_names):
        self.name = random.choice(AI_names)

    # Function to get AI's gesture
    def get_gesture(self):
        return random.randint(range(5)) #