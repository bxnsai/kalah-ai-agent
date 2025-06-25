''' Runs the Kalah game '''
from games import *

class Kalah(Game):
    OPPOSITE_PITS = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7,
                     7: 5, 8: 4, 9: 3, 10: 2, 11: 1, 12: 0}

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


        landing_index = -1  # track where the last stone lands

        # distribute stones
        while stones > 0:
            index = (index + 1) % 14
            # Skip opponent's store
            if state.to_move == 'MAX' and index == 13:
                continue
            if state.to_move == 'MIN' and index == 6:
                continue
            new_board[index] += 1
            stones -= 1
            landing_index = index

        # check for capture
        if state.to_move == 'MAX':
            if landing_index == 6:
                again = True
            elif 0 <= landing_index <= 5 and new_board[landing_index] == 1:
                opp_index = self.OPPOSITE_PITS[landing_index]
                if new_board[opp_index] > 0:
                    new_board[6] += new_board[opp_index] + 1
                    new_board[opp_index] = 0
                    new_board[landing_index] = 0

        elif state.to_move == 'MIN':
            if landing_index == 13:
                again = True
            elif 7 <= landing_index <= 12 and new_board[landing_index] == 1:
                opp_index = self.OPPOSITE_PITS[landing_index]
                if new_board[opp_index] > 0:
                    new_board[13] += new_board[opp_index] + 1
                    new_board[opp_index] = 0
                    new_board[landing_index] = 0


        # determine next player
        next_player = state.to_move if again else ('MIN' if state.to_move == 'MAX' else 'MAX')

        # get available moves for next player
        if next_player == 'MAX':
            moves = [i for i in range(6) if new_board[i] > 0]
        else:
            moves = [i for i in range(7, 13) if new_board[i] > 0]

        # sweep 
        if self.terminal_test(GameState(to_move=next_player, utility=0, moves=moves, board=new_board)):
            new_board[6] += sum(new_board[:6])  # MAX collects all seeds in its pits
            new_board[13] += sum(new_board[7:13])  # MIN collects all seeds in its pits
            for i in range(0, 6): new_board[i] = 0 # set MAX pits to 0
            for i in range(7, 13): new_board[i] = 0 # set MIN pits to 0
            utility = new_board[6] - new_board[13]
        else:
            utility = 0

        return GameState(to_move=next_player, utility=utility, moves=moves, board=new_board)



    def utility(self, state, player) -> int:
        if self.terminal_test(state):
            max_score = state.board[6]
            min_score = state.board[13]
            return (max_score - min_score) if player == 'MAX' else (min_score - max_score)

        return 0 # Game is not over, utility is 0

    def terminal_test(self, state) -> bool:
        # Check if either player has no seeds left in their pits
        return all(i == 0 for i in state.board[:6]) or all(i == 0 for i in state.board[7:13])

    def display(self, state):
        board = state.board
        side1 = tuple(board[:7])
        side2 = tuple(board[7:])
        print("Current Board:",side1, side2) 

    def play_game(self, *players): # have to overide play_game to handle extra turns
        """Play an n-person, move-alternating game, respecting extra turns."""
        state = self.initial
        while True:
            self.display(state)
            current_player = players[0] if state.to_move == 'MAX' else players[1]
            move = current_player(self, state)
            state = self.result(state, move)


            if self.terminal_test(state):
                self.display(state)
                return self.utility(state, 'MIN')  # Or 'MIN', depending on who you want the score from


if __name__ == '__main__':
    kalah = Kalah()

    utility = kalah.play_game(query_player, alpha_beta_player)

    if utility < 0:
        print("You win!")
    elif utility > 0:
        print("You lose!")
    else:
        print("It's a draw!")
