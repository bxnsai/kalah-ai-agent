''' Runs the Kalah game '''
from games import *

class Kalah(Game):
    def __init__(self): 
        board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        moves = [0,1,2,3,4,5]
        self.initial = GameState(to_move='MAX',utility=0, moves=moves,board=board)

    def actions(self, state):
        choice = []
        if state.to_move == 'MAX':
            for i in range(6):
                if state.board[i] > 0:
                    choice.append(i)
        elif state.to_move == 'MIN':
            for i in range(7, 13):
                if state.board[i] > 0:
                    choice.append(i)
                    
        return choice 

    def result(self, state, move):
        pass 

    def utility(self, state, player):
        if self.terminal_test(state):
            max_score = state.board[6]
            min_score = state.board[13]
            return (max_score - min_score) if player == 'MAX' else (min_score - max_score)


    def terminal_test(self, state) -> bool:
        # Check if either player has no seeds left in their pits
        return all(i == 0 for i in state.board[:6]) or all(i == 0 for i in state.board[7:13])

    def display(self, state):
        pass 



if __name__ == '__main__':
    kalah = Kalah()

    # utility = kalah.play_game(query_player,alpha_beta_cutoff_search)

    # display results 
