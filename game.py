from human import Human
from ai import AI
import random
import re
import os


class Game():
    # Function to initialize 
    def __init__(self):
        self.turn = 0
        self.round = 1
        self.players = [] 
        self.game_mode = ""
        self.game_mode_var = ""
        self.eliminated_players = []
        self.reserved_names = ["Siri", "Alexa", "Bixby", "Google", "Bing"]
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
            self.players_no = re.sub(rf"[^2-5]", "", input("Select how many players (2 or 3): "))

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
            print("\nSelect game mode (rounds):\n1. Best of 3\n2. Best of 5\n3. Best of 7")
            self.game_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))
        self.rounds = int(self.game_mode) * 2 + 1
        self.game_mode_var = ""
        if self.players_no == '3':
            while len(self.game_mode_var) != 1:
                self.tie = "3" if self.game_mode == '1' else "2"
                print(f"\nSelect game mode variation:\n1. Elimination (First two players to win 1 round move on)\n2. Tie Breaker (In case of a "
                    f"{self.tie}-way tie, tie breaker round decides winner)")
                self.game_mode_var = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode variation "))

    # Function to obtain player gestures.
    def rock_paper_scissors_lizard_spock(self):
        while self.round - 1 != self.rounds:
            self.get_round_turn()
            self.get_players()
            self.get_gestures()
            self.display_gestures()
            self.check_gestures()
            self.get_wins()
            self.get_winner()
            self.display_status()
            self.reset()
        self.display_end_game_stats()

    # Function to obtain round and turn of current game.
    def get_round_turn(self):
        print(f"\nRound {self.round}.{self.turn}")

    # Function to build list of players.
    def get_players(self):
        if self.turn == 0:
            self.players_list = self.players
        elif self.turn > 0:
            self.players_list = [self.players_list[i] for i in self.max_ndx]
        
    # Function to obtain players' gestures
    def get_gestures(self):
        for player in self.players_list:
            player.get_gesture()

    # Function to show players' gestures.
    def display_gestures(self):
        for player in self.players_list:
            print(f"{player.name} selected {player.gesture}")

    # Function to check players' gestures against each other.
    def check_gestures(self):
        self.remaining_players = [player for player in self.players_list]
        for player in self.remaining_players:
            self.current_player = player
            for rem_player in self.remaining_players:
                self.current_player.check_gesture(rem_player)

    # Function to obtain players' wins.
    def get_wins(self):
        self.round_wins = [player.wins for player in self.players_list]

    # Function to obtain winner by getting all players' round wins.
    def get_winner(self):
        self.winner = ""
        self.max_wins = max(self.round_wins)
        self.max_ndx = [i for i, wins in enumerate(self.round_wins) if wins == self.max_wins]
        if len(self.max_ndx) == 1:
            self.winner = self.players_list[self.max_ndx[0]]
            self.winner.add_total_win()
            self.check_for_eliminating_player()
        
    # Function to eliminate losing player in game mode Elimination
    def check_for_eliminating_player(self):
        if len(self.players) == 3 and self.game_mode_var == "1": 
            self.players_w_wins = [player for player in self.players if player.total_wins > 0]
            if len(self.players_w_wins) == 2:
                self.eliminated_players = [player for player in self.players if player not in self.players_w_wins]
                self.players = [player for player in self.players_w_wins]
        
    # Function to display round.turn results.
    def display_status(self):
        if self.winner:
            print(f"\nRound {self.round} winner is {self.winner.name}!")
        elif len(self.max_ndx) > 1:
            status = f"{self.players_list[self.max_ndx[0]].name} and {self.players_list[self.max_ndx[1]].name}" if len(self.max_ndx) == 2 else\
                f"{self.players_list[self.max_ndx[0]].name}, {self.players_list[self.max_ndx[1]].name} and "\
                f"{self.players_list[self.max_ndx[2]].name}"
            print(f"\nIts a tie! {status} will play again!")
        for player in self.eliminated_players:
            print(f"Player {player.name} has been eliminated!")
            del self.eliminated_players[0]
        os.system('pause')

    # Function to reset game stats.
    def reset(self):
        if self.winner:
            self.round += 1
            self.turn = 0
        elif len(self.max_ndx) > 1:
            self.turn += 1
        for player in self.players:
                player.wins = 0

    # Function to show end game stats
    def display_end_game_stats(self):
        print("\nEnd Game Stats")
        for player in self.players:
            print(f"{player.name} total wins: {player.total_wins}")
