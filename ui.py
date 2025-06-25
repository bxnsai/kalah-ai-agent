# User Interface for Kalah
from tkinter import Tk
from kalah import Kalah


class KalahUI:
    def __init__(self):
        self.game = Kalah()
        self.drawBoard()
        self.update_board()

    def drawBoard(self):
        self.state = self.game.initial 
        self.window = Tk()
        self.window.title("Kalah Game")
        self.create_widgets()
        self.window.mainloop()

    def updateBoard(self):
        # Update the UI based on the current game state
        pass  # Placeholder for actual board update code

    def clickHandler(self): # determines which pit was clicked & validates 
        pass 

    def performMove(self): # updates board & calls AI if needed 
        pass 

    def showWinner(self): # displays winner of game 
        pass 

    def resetGame(self):
        pass 

if __name__ == "__main__":

    ui = KalahUI()  # Initialize the UI with the game instance