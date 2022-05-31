from human import Human
from ai import AI
import random
import re


class Game():
    # Function to initialize 
    def __init__(self):
        self.players = []
        self.user_selected_mode = ""  
        self.reserved_names = ["Siri", "Alexa", "Bixby"]
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    # Function to run game.
    def run_game(self):
        self.display_welcome()
        self.select_game_mode()
        self.select_players()
        self.display_players()

    # Function to display welcome.
    def display_welcome(self):
        print("\nRock, Paper, Scissors, Lizard, Spock\n\nSAM KASS: Welcome to exciting world of Rock, Paper, Scissors, Lizard, Spock. I am your "
            "cohost Sam Kass...\nKAREN BRYLA: And I am your other cohost Karen Bryla, here for another game of ... \nUNISON: Rock, Paper, "
            "Scissors, Lizard, Spock!\nKAREN BRYLA: The rules are simple")
        self.display_rules()

    # Function to display game rules.
    def display_rules(self):
        print("\n\nRules of the Game:")
        print(f"{self.gestures[0]} crushes {self.gestures[2]}")
        print(f"{self.gestures[2]} cuts {self.gestures[1]}")
        print(f"{self.gestures[1]} covers {self.gestures[0]}")
        print(f"{self.gestures[0]} decimates {self.gestures[3]}")
        print(f"{self.gestures[3]} poisons {self.gestures[4]}")
        print(f"{self.gestures[4]} smashes {self.gestures[2]}")
        print(f"{self.gestures[2]} decapitates {self.gestures[3]}")
        print(f"{self.gestures[3]} eats {self.gestures[1]}")
        print(f"{self.gestures[1]} disproves {self.gestures[4]}")
        print(f"{self.gestures[4]} vaporizes {self.gestures[0]}")

    # Function to select game mode.
    def select_game_mode(self):
        while not(self.user_selected_mode):
            print("\nSelect game mode:\n1. 2 Players\n2. 3 Players\n3. Random ")
            self.user_selected_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))
            if self.user_selected_mode == "3":
                self.user_selected_mode = random.randint(1, 2)

    # Function to select list of players. 
    def select_players(self):
        random.shuffle(self.reserved_names)
        ndex = 0
        for i in range(0, int(self.user_selected_mode) + 1):
            self.player_type = ""
            while not(self.player_type):
                print(f"\nSelect Player {i+1} type:\n1. Human\n2. AI")
                self.player_type = re.sub(rf"[^1-2]", "", input("\nPlayer selects type ")).title()            
            if int(self.player_type) == 1:
                self.player = Human(self.players)
                self.player.get_name()
                self.players.append(self.player)
            else:
                self.players.append(AI(self.reserved_names[ndex]))
                ndex += 1

    # Function to display list of players:
    def display_players(self):
        print("\nList of players:")
        for i, player in enumerate(self.players):
            print(f"Player {i+1} name: {player.name}")

            
          