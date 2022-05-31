from human import Human
from ai import AI
import random
import re


class Game():
    # Function to initialize 
    def __init__(self):
        self.players = [] 
        self.game_mode = ""
        self.game_mode_var = ""
        self.turn = 1
        self.round = 1
        self.reserved_names = ["Siri", "Alexa", "Bixby"]
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    # Function to run game.
    def run_game(self):
        self.display_welcome()
        self.select_player_number()
        self.select_players()
        self.display_players()
        self.get_game_mode()
        self.rock_paper_scissors_lizard_spock()

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
        self.players_no = ""
        while len(self.players_no) != 1:
            self.players_no = re.sub(rf"[^2-3]", "", input("Select how many players (2 or 3): "))

    # Function to select list of players. 
    def select_players(self):
        random.shuffle(self.reserved_names)
        self.ndex = 0
        for i in range(0, int(self.players_no)):
            self.player_type = ""
            while len(self.player_type) != 1:
                print(f"\nSelect player {i+1} type:\n1. Human\n2. AI")
                self.player_type = re.sub(rf"[^1-2]", "", input("\nPlayer selects type ")).title()            
            if self.player_type == '1':
                self.player = Human(self.players)
                self.player.get_name()
                self.players.append(self.player)
            else:
                self.players.append(AI(self.reserved_names[self.ndex]))
                self.ndex += 1

    # Function to display list of players.
    def display_players(self):
        print("\nList of players:")
        for i, player in enumerate(self.players):
            print(f"Player {i+1}: {player.name}")

    # Function to obtain game mode.
    def get_game_mode(self):
        self.game_mode = ""
        while len(self.game_mode) != 1:
            print("\nSelect game mode:\n1. Best of 3\n2. Best of 5\n3. Best of 7")
            self.game_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))
        self.rounds = int(self.game_mode) * 2 + 1
        self.game_mode_var = ""
        if self.players_no == '3':
            while len(self.game_mode_var) != 1:
                self.tie = "3" if self.game_mode == '1' else "2"
                print(f"\nSelect game mode variation:\n1. Elimination (First two players to win 1 round move on)\n2. Tie Breaker (In case of a "
                    f"{self.tie}-way tie, tie breaker round decides winner)")
                self.game_mode_var = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode "))

    # Function to obtain player gestures.
    def rock_paper_scissors_lizard_spock(self):
        print("Round")
        self.get_players()
        self.get_gestures()
        self.display_gestures()

    # Function to get round and turn of current game.
    #def get_round_turn(self):
    #    self.rounds = int(self.game_mode)

    # Function to build list of players.
    def get_players(self):
        self.players_list = self.players
        print(self.players_list)
        
    # Function to obtain players' gestures
    def get_gestures(self):
        for player in self.players_list:
            player.get_gesture()

    # Function to display players' gestures.
    def display_gestures(self):
        print("Players gestures")
        for player in self.players_list:
            print(f"{player.name}: {player.gesture}")

    # Function to check players' gestures against each other.
    def check_gestures(self):
        for player in self.players_list:
            self.current_player = player
            self.remaining_players = [rem_player for rem_player in self.players_list if rem_player != self.current_player]
            for rem_player in self.remaining_players:
                player.check_gesture(rem_player)

    # Function to capture players' win and lose status.
    def capture_win_lose(self):
        self.winners = []
        self.losers = []
        for player in self.players_list:
            if player.win == True:
                self.winners.append(player)
            if player.lose == True:
                self.losers.append(player)

    # Function to determine if their is a winner