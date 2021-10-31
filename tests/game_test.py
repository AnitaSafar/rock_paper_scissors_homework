import unittest
from models.game import *
from models.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        player1 = Player("Erin", "rock")
        player2 = Player("Hugo", "scissors")
        self.game = Game(player1, player2)

    # def test_no_random_choice(self):
        























    # def test_first_player_has_name(self):
    #     self.assertEqual("Erin", self.game.player1.name)

    # def test_game_has_second_player(self):
    #     self.assertEqual("Hugo", self.game.player2.name)
    
    # def test_first_players_choice(self):
    #     self.assertEqual("rock", self.game.player1.choice)
   
    # def test_second_players_choice(self):
    #     self.assertEqual("scissors", self.game.player2.choice)
    
    # def test_rock_wins(self):
    #     result = rock_wins(self.game.player1.choice, self.game.player2.choice)
    #     self.assertEqual("rock", result)