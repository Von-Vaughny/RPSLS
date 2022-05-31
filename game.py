from human import Human
from ai import AI
import random
import re


class Game():
    # Function to initialize 
    def __init__(self):
        self.players = [] 
        self.players_no = "" 
        self.game_mode = ""
        self.game_mode_var = ""
        self.reserved_names = ["Siri", "Alexa", "Bixby"]
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    # Function to run game.
    def run_game(self):
        self.display_welcome()
        self.select_player_number()
        self.select_players()
        self.display_players()
        self.get_game_mode()

    # Function to display welcome.
    def display_welcome(self):
        print("\n********************************* Rock, Paper, Scissors, Lizard, Spock **********************************\n")
        print("SAM KASS: Welcome to exciting world of Rock, Paper, Scissors, Lizard, Spock. I am your cohost Sam Kass...")
        print("KAREN BRYLA: And I am your cohost Karen Bryla, here for another game of ... ")
        print("UNISON: Rock, Paper, Scissors, Lizard, Spock!")
        print("KAREN BRYLA: The rules are simple")
        self.display_rules()

    # Function to display game rules.
    def display_rules(self):
        print("\n\nRULES OF THE GAME")
        print(f"{self.gestures[0]} crushes {self.gestures[2]}")
        print(f"{self.gestures[2]} cuts {self.gestures[1]}")
        print(f"{self.gestures[1]} covers {self.gestures[0]}")
        print(f"{self.gestures[0]} decimates {self.gestures[3]}")
        print(f"{self.gestures[3]} poisons {self.gestures[4]}")
        print(f"{self.gestures[4]} smashes {self.gestures[2]}")
        print(f"{self.gestures[2]} decapitates {self.gestures[3]}")
        print(f"{self.gestures[3]} eats {self.gestures[1]}")
        print(f"{self.gestures[1]} disproves {self.gestures[4]}")
        print(f"{self.gestures[4]} vaporizes {self.gestures[0]}\n")

    # Function to select game mode.
    def select_player_number(self):
        while not(self.players_no):
            self.players_no = re.sub(rf"[^2-3]", "", input("Select how many players (2 or 3): "))

    # Function to select list of players. 
    def select_players(self):
        random.shuffle(self.reserved_names)
        for i in range(0, int(self.players_no)):
            ndex = 0
            self.player_type = ""
            while not(self.player_type):
                print(f"\nSelect player {i+1} type:\n1. Human\n2. AI")
                self.player_type = re.sub(rf"[^1-2]", "", input("\nPlayer selects type ")).title()            
            if self.player_type == '1':
                self.player = Human(self.players)
                self.player.get_name()
                self.players.append(self.player)
            else:
                self.players.append(AI(self.reserved_names[ndex]))
                ndex += 1

    # Function to display list of players.
    def display_players(self):
        print("\nList of players:")
        for i, player in enumerate(self.players):
            print(f"Player {i+1}: {player.name}")

    # Function to obtain game mode.
    def get_game_mode(self):
        while not(self.game_mode):
            print("\nSelect game mode:\n1. Best of 3\n2. Best of 5\n3. Best of 7")
            self.game_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))
        while not(self.game_mode_var):
            if self.players_no == '3':
                self.tie = "3" if self.game_mode == '1' else "2"
                print(f"\nSelect game mode variation:\n1. Elimination (First two players to 1 win move on)n2. Tie Breaker (In case of a "
                    f"{self.tie}-way tie, tie breaker round)")
                self.game_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))