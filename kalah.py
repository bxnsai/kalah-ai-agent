''' Runs the Kalah game '''
from games import *

class Kalah(Game):
    def __init__(self): 
        board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        moves = [0,1,2,3,4,5]
        self.initial = GameState(to_move='MAX',moves=moves,board=board)

    def actions(self, state):
        pass 

    def result(self, state, move):
        pass 

    def utility(self, state, player):
        pass 

    def terminal_test(self, state):
        pass 

    def display(self, state):
        pass 



if __name__ == '__main__':
    kalah = Kalah()

    utility = kalah.play_game(query_player,alpha_beta_cutoff_search)

    # display results 
