import math
import random

class Player:
    def __init__(self, letter):
        # letter é x ou o do jogo da velha (tic-tac-toe em inglês)
        self.letter = letter

        # we want all players to get their next move
        def get_move(self,game):
            pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        square = random.choice(list(game.available_moves()))
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ") 
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True # if these are successful, then yay!
            except ValueError:
                print('Invalid Square. Try again.')
        
        return val