import unittest
from models.player import *
from models.game import Game

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Erin", "rock")
        self.player2 = Player("Helen", "paper")

    def test_player_has_name(self):
        self.assertEqual("Erin", self.player1.name)
    
    def test_player_has_choice(self):
        self.assertEqual("rock", self.player1.choice)

    # def test_no_random_choice(self):
    


   
   
    
    
    
