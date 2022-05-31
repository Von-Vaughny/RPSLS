from human import Human
from ai import AI
import random
import re


class Game():
    # Function to initialize 
    def __init__(self):
        self.players = []
        self.AI_names = ["Siri", "Alexa", "Bixby"]
        self.user_selected_mode = ""  

    # Function to run game.
    def run_game(self):
        self.display_welcome()
        self.select_game_mode()
        self.select_players()

    # Function to display welcome.
    def display_welcome(self):
        print("Rock, Paper, Scissors, Lizard, Spock\n\nSAM KASS: Welcome to exciting world of Rock, Paper, Scissors, Lizard, Spock. I am your "
            "cohost Sam Kass...\nKAREN BRYLA: And I am your other cohost Karen Bryla, here for another game of ... \nUNISON: Rock, Paper, "
            "Scissors, Lizard, Spock!")

    # Function to select game mode.
    def select_game_mode(self):
        while not(self.user_selected_mode):
            print("\nSelect game mode:\n1. 2 Players\n2. 3 Players")
            self.user_selected_mode = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode "))

    # Function to select list of players. 
    def select_players(self):
        for i in range(0, int(self.user_selected_mode) + 1):
            self.player_type = ""
            while not(self.player_type):
                print("\nSelect player type:\n1. Human\n2. AI")
                self.player_type = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode "))            
            self.players.append(Human()) if int(self.player_type) == 1 else self.players.append(AI())