from game import Game
from replay import Replay


replay = True

while replay:
    game = Game()
    game.run_game()
    replay = Replay().replay()