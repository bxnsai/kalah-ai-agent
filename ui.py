# User Interface for Kalah
from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem
from PyQt6.QtGui import QBrush, QPen, QColor, QPainterPath, QFont, QPainter, QPixmap
from PyQt6.QtCore import QRectF,Qt
import random
import os 

class KalahUI(QMainWindow):

    def __init__(self,game):
        super().__init__()
        self.game = game  # Store the game instance
        self.state = game.initial
        self.setWindowTitle("Kalah Game")
        self.setGeometry(100, 100, 1010, 600)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setCentralWidget(self.view)
        self.stone_pixmaps = []
        for i in range(1, 7):
            path = f"beads/bead{i}.png"
            if os.path.exists(path):
                self.stone_pixmaps.append(QPixmap(path).scaled(20,20))
        self.drawBoard()

    def drawBoard(self):
        self.scene.clear()

        # Colors and pens
        black_pen = QPen(Qt.GlobalColor.black)
        white_brush = QBrush(Qt.GlobalColor.white)
        board_brush = QBrush(QColor("black"))
        gray_brush = QBrush(QColor("lightgray"))

        # Background (outer gray)
        self.scene.addRect(QRectF(0, 0, 1000, 600), black_pen, gray_brush)

        # Rounded black board background
        path = QPainterPath()
        path.addRoundedRect(QRectF(10, 139, 980, 309), 75, 75)
        self.scene.addPath(path, black_pen, board_brush)

        board = self.game.initial.board

        # Stores
        self.scene.addEllipse(QRectF(27, 178, 120, 220), black_pen, white_brush)     # Left (AI)
        self.scene.addEllipse(QRectF(847, 178, 120, 220), black_pen, white_brush)    # Right (Player)
        

        # Pits (6 top row for AI, 6 bottom row for Player)
        for i in range(6):
            x = 147 + i * 119
            self.scene.addEllipse(QRectF(x, 183, 105, 105), black_pen, white_brush)  # AI row (top)
            self.scene.addEllipse(QRectF(x, 293, 105, 105), black_pen, white_brush)  # Player row (bottom)

            # AI pits labels
            pit_label = self.scene.addText(f"{self.state.board[7 + i]}", QFont("Arial", 24))
            pit_label.setDefaultTextColor(Qt.GlobalColor.white)
            pit_label.setPos(187 + i * 119, 154)

            # Player pits labels
            pit_label = self.scene.addText(f"{self.state.board[i]}", QFont("Arial", 24))
            pit_label.setDefaultTextColor(Qt.GlobalColor.white)
            pit_label.setPos(187 + i * 119, 402)

        # Turn Label
        turn_label = self.scene.addText("Your Turn", QFont("Arial", 16, QFont.Weight.Bold))
        turn_label.setDefaultTextColor(Qt.GlobalColor.red)
        turn_label.setPos(459, 107)

        # Score labels
        ai_score = self.scene.addText(("AI Score: " + str(board[13])), QFont("Arial", 24))
        ai_score.setDefaultTextColor(Qt.GlobalColor.black)
        ai_score.setPos(76, 463)

        player_score = self.scene.addText(("Your Score: " + str(board[6])), QFont("Arial", 24))
        player_score.setDefaultTextColor(Qt.GlobalColor.black)
        player_score.setPos(795, 463)

        if self.stone_pixmaps:
            board = self.state.board
            # AI Store stones
            for i, store_index in enumerate([13, 6]):
                for _ in range(board[store_index]):
                    x = random.randint(50, 110) if i == 0 else random.randint(870, 920)
                    y = random.randint(210, 370)
                    bead = QGraphicsPixmapItem(random.choice(self.stone_pixmaps))
                    bead.setPos(x, y)
                    self.scene.addItem(bead)

            #AI Pits 
            for i in range(6): 
                count = board[7 + i] 
                for _ in range(count):
                    x = random.randint((175 + i * 119),225 + i * 119)
                    y = random.randint(211, 261)
                    bead = QGraphicsPixmapItem(random.choice(self.stone_pixmaps))
                    bead.setPos(x, y)
                    self.scene.addItem(bead)

            # Player Pits
            for i in range(6):
                count = board[5 - i]
                for _ in range(count):
                    x = random.randint((175 + i * 119),225 + i * 119)
                    y = random.randint(321, 371)
                    bead = QGraphicsPixmapItem(random.choice(self.stone_pixmaps))
                    bead.setPos(x, y)
                    self.scene.addItem(bead)
            
        else:
            print(f"No bead images found")

    def updateBoard(self): # updates pit counts, shows whose turn it is, etc.
        # two lists for pit labels and counts

        # fill according to state, maybe view the dropping of seeds and show that 
        pass 


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