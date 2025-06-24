''' Runs the Kalah game '''
from games import *

class Kalah(Game):
    def __init__(self): 
        board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        moves = [0,1,2,3,4,5]
        self.initial = GameState(to_move='MAX',utility=0, moves=moves,board=board)

    def actions(self, state) -> list:
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

    def result(self, state, move) -> 'GameState':
        index = move 
        stones = state.board[move]
        new_board = list(state.board)
        new_board[move] = 0  # set value in selected store to 0
        next_player = None
        again = False 
        moves = []

        while stones > 0:
            index = (index + 1) % 14  # move to the next pit to wrap around the board

            # skip the opponent's store
            if state.to_move == 'MAX' and index == 13: continue 
            if state.to_move == 'MIN' and index == 6: continue

            if state.to_move == 'MAX':
                new_board[index] += 1
                stones -= 1
                if stones == 0 and index == 6: # check if last stone is dropped in own store
                    next_player = 'MAX'
                    again = True

            if state.to_move == 'MIN':
                new_board[index] += 1
                stones -= 1
                if stones == 0 and index == 13: # check if last stone is dropped in own store
                    next_player = 'MIN'
                    again = True
        
        if not again: next_player = 'MIN' if state.to_move == 'MAX' else 'MAX'
        if next_player == 'MAX':
            moves = [i for i in range(6) if new_board[i] > 0]
        elif next_player == 'MIN':
            moves = [i for i in range(7, 13) if new_board[i] > 0]


        return GameState(to_move=next_player, utility=0, moves=moves, board=new_board)



    def utility(self, state, player) -> int:
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
