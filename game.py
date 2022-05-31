import random


class Game():
    # Function to 
    def __init__(self):
        self.AI_names = random.shuffle(["Siri", "Alexa", "Bixby"])

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Rock, Paper, Scissors, Lizard, Spock\n\nSAM KASS: Welcome to exciting world of Rock, Paper, Scissors, Lizard, Spock. I am your "
            "cohost Sam Kass...\nKAREN BRYLA: And I am your other cohost Karen Bryla, here for another game of ... \nUNISON: Rock, Paper, "
            "Scissors, Lizard, Spock!")