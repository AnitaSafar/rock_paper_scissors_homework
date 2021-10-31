# from models.player import Player

class Game():

    def __init__(self):
        pass
    # def __init__(self, player1, player2):
    #     self.player1 = player1
    #     self.player2 = player2

    
    def winning_player(self, player1, player2):
        if player1.choice != player2.choice:
            if player1.choice == "rock" and player2.choice == "scissors":
                return f'{player1.name} is the winner!'
            elif player1.choice == "scissors" and player2.choice == "paper":
                return f'{player1.name} is the winner!'
            elif player1.choice == "paper" and player2.choice == "rock":
                return f'{player1.name} is the winner!'
            else:
                return f'{player2.name} is the winner!'
        else:
            return "It's a draw!"
    
# print(Game().winning_player("scissors", "paper"))

   