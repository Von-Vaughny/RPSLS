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
        self.stop = False
        self.tie_breaker = False
        self.players = [] 
        self.eliminated_players = []
        self.gestures = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    # Function to run game.
    def run_game(self):
        self.display_welcome()
        self.display_rules()
        self.select_player_no()
        self.select_players()
        self.display_players()
        self.get_game_mode()
        self.get_game_mode_var()
        self.rock_paper_scissors_lizard_spock()

    # Function to display welcome.
    def display_welcome(self):
        print("\n********************************* Rock, Paper, Scissors, Lizard, Spock **********************************\n")
        print("SAM KASS: Welcome to exciting world of Rock, Paper, Scissors, Lizard, Spock. I am your cohost Sam Kass...")
        print("KAREN BRYLA: And I am your cohost Karen Bryla, here for another game of ... ")
        print("IN UNISON: Rock, Paper, Scissors, Lizard, Spock!")
        print("KAREN BRYLA: The rules are simple")

    # Function to display game rules.
    def display_rules(self):
        print("\nRULES OF THE GAME")
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

    # Function to select number of players.
    def select_player_no(self):
        self.players_no = ""
        while (len(self.players_no) < 1):
            self.players_no = re.sub(rf"[^0-9]", "", input("SAM KASS: How many players (2 or 3) will play? "))

    # Function to select list of players. // Refactor? 
    def select_players(self):
        # .py for reserved names???
        reserved_names = ["Siri", "Alexa", "Bixby", "Google", "Bing", "Firefox", "Opera", "Windows", "Safari", "Tor"]
        random.shuffle(reserved_names)
        name_ndex = 0
        name_cycle_ndex = 0
        for i in range(0, int(self.players_no)):
            self.player_type = ""
            while len(self.player_type) != 1:
                print(f"\nKAREN BRYLA: Select player {i+1} type:\n1. Human\n2. AI")
                self.player_type = re.sub(rf"[^1-2]", "", input("\nPlayer selects type "))            
            if self.player_type == '1':
                self.player = Human()
                self.player.get_name(self.players, reserved_names)
                self.players.append(self.player)
            else:
                if (name_ndex >= len(reserved_names)):
                    name_cycle_ndex += 1
                    name_ndex = 0
                self.players.append(AI(reserved_names[name_ndex] + f"_{name_cycle_ndex}"))
                name_ndex += 1
            
    # Function to display list of players.
    def display_players(self):
        print("\nSAM KASS: In today's match we have the following players:")
        for i, player in enumerate(self.players):
            print(f"Player {i+1}: {player.name}")

    # Function to obtain game mode and game mode settings.
    def get_game_mode(self):
        self.game_mode = ""
        while len(self.game_mode) != 1:
            print("\nKAREN BRYLA: Select game mode (rounds):\n1. Best of 3\n2. Best of 5\n3. Best of 7")
            self.game_mode = re.sub(rf"[^1-3]", "", input("\nPlayer selects game mode "))
        self.rounds = int(self.game_mode) * 2 + 1
        self.wins_needed = 4 if self.game_mode == '3' else 3 if self.game_mode == '2' else 2

    # Function to obtain game mode variation and game mode variation setttings.
    def get_game_mode_var(self):
        self.game_mode_var = ""
        while len(self.game_mode_var) != 1:
            print("\nSAM KASS: Select game mode variation: \n1. Tie Breaker (In case of a tie, tie breaker round decides winner)"\
                "\n2. Elimination (First two players to win 1 round move on)\nConsidering Doublefist variation")
            if (int(self.players_no) >= self.rounds):
                print("Considering Elimination w/Tie Breaker")
            self.game_mode_var = re.sub(rf"[^1-2]", "", input("\nPlayer selects game mode variation "))
        if (self.game_mode_var == "2"):
            self.players_remaining_no = int(self.game_mode) * 2

    # Function to obtain player gestures.
    def rock_paper_scissors_lizard_spock(self):
        while self.round:
            self.get_round_turn()
            self.get_players()
            self.get_gestures()
            self.check_gestures()
            self.display_gestures()
            self.get_winner()
            self.display_status()
            self.set()
        self.display_end_game_stats()

    # Function to obtain round and turn of current game.
    def get_round_turn(self):
        print(f"\nRound {self.round}.{self.turn} {'(Tie Breaker)' if self.round > self.rounds else ''}")

    # Function to build list of players.
    def get_players(self):
        self.players_list = self.players if self.turn == 0 else [self.players_list[i] for i in self.max_turn_ndx]

    # Function to obtain players' gestures
    def get_gestures(self):
        for player in self.players_list:
            player.get_gesture()

    # Function to check players' gestures against each other. // Refactor with gestures class
    def check_gestures(self):
        players = [player for player in self.players_list]
        for player in self.players_list:
            remaining_players = [rem_player for rem_player in players if rem_player != player]
            for remaining_player in remaining_players:
                player.check_gesture(remaining_player)
            del players[0] 

    # Function to show players' gestures.
    def display_gestures(self):
        print()
        for player in self.players_list:
            print(f"{player.name} selected {player.gesture} (turn wins: {player.turn_wins}, round wins: {player.round_wins}) ")

    # Function to obtain round winner based on the max number of wins attained during the turn.
    def get_winner(self):
        self.winner = ""
        self.turn_wins = [player.turn_wins for player in self.players_list]
        self.max_wins = max(self.turn_wins)
        self.max_turn_ndx = [i for i, wins in enumerate(self.turn_wins) if wins == self.max_wins]
        if len(self.max_turn_ndx) == 1:
            self.winner = self.players_list[self.max_turn_ndx[0]]
            self.winner.add_round_win()
            self.check_game_mode()
            
    # Function to check result of game mode.
    def check_game_mode(self):
        if self.game_mode_var == "1" and self.round >= self.rounds:
            self.check_for_tie_breaker_players()
        elif self.game_mode_var == "2" and self.round < self.rounds:
            self.check_for_eliminated_players()
        # elif self.game_mode == "3"
        # elif self.game_mode == "4":

    # Function to determine players for tie breaker round in game mode Tie Breaker. // Refactor
    def check_for_tie_breaker_players(self):
        self.tie_breaker = False
        round_wins = [player.round_wins for player in self.players_list]
        self.max_round_wins = max(round_wins)
        self.max_round_ndx = [i for i, wins in enumerate(round_wins) if wins == self.max_round_wins]
        print(round_wins)
        if len(self.max_round_ndx) > 1 and self.round == self.rounds:
            self.players = [self.players_list[i] for i in self.max_round_ndx]
        elif len(self.max_round_ndx) == 1:
            self.stop = True

    # Function to eliminate player(s) not hitting win minimum in game mode Elimination.
    def check_for_eliminated_players(self):
        self.players_w_wins = [player for player in self.players if player.round_wins >= 1]
        if (len(self.players_w_wins) == 2): 
            self.eliminated_players = [player for player in self.players if player not in self.players_w_wins]
            self.players = [player for player in self.players_w_wins]

    # Function to display round.turn results.
    def display_status(self):
        players_who_won = [player.name for player in self.players_list if player.round_wins == self.max_round_wins] if\
            (self.round == self.rounds and self.turn == 0) else [player.name for player in self.players_list if player.turn_wins == self.max_wins]
        statusTemp = "Its a tie! " + ', '.join(map(str, players_who_won))
        status = " and ".join(statusTemp.rsplit(", ", 1)) + (" will battle it out in a Tie Breaker round" if\
            (self.round == self.rounds and self.turn == 0) else " will play again!")       
        if self.winner:
            print(f"\nRound {self.round} winner is {self.winner.name}!") 
        if (self.round == self.rounds and self.turn == 0) or not(self.winner): 
                print(f"\n{status}")  
        for player in self.eliminated_players:
            print(f"{player.name} has been eliminated!")
        self.eliminated_players = ""
        os.system('pause')

    # Function to set game parameters.
    def set(self):
        # If there is a winner, reset round.turn and increment round.
        if self.winner:
            self.round += 1
            self.turn = 0
        # If there is a turn tie, increment turn.
        elif len(self.max_turn_ndx) > 1:
            self.turn += 1
        # Reset all player.turn_wins stats.
        for player in self.players:
            player.turn_wins = 0
        # If any player has reached the number of wins needed to win match, stop the match.
        for player in self.players:
            if player.round_wins == self.wins_needed:
                self.round = 0
        # If no player has reached the number of wins needed to win match in Tie Breaker Mode, winner is the player with the most wins.
        if self.stop or self.round == self.rounds + 2:
            self.winner = self.players_list[self.max_round_ndx[0]]
            self.round = 0

    # Function to show end game stats
    def display_end_game_stats(self):
        print("\nEnd Game Stats")
        for player in self.players:
            print(f"{player.name} total wins: {player.round_wins}")
        print(f"\n{self.winner.name} takes the match!")