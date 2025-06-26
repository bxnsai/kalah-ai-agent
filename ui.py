# User Interface for Kalah
from kalah import Kalah
from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView
from PyQt6.QtGui import QBrush, QPen, QColor, QPainterPath, QFont, QPainter
from PyQt6.QtCore import QRectF,Qt

class KalahUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kalah Game")
        self.setGeometry(100, 100, 1010, 600)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene, self)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setCentralWidget(self.view)

        self.game = Kalah()  # Initialize the Kalah game instance
        self.drawBoard()


    def drawBoard(self):
        self.scene.clear()

        # Colors and pens
        black_pen = QPen(Qt.GlobalColor.black)
        white_brush = QBrush(Qt.GlobalColor.white)
        board_brush = QBrush(QColor("black"))
        gray_brush = QBrush(QColor("lightgray"))

        # Background (outer gray)
        background = self.scene.addRect(QRectF(0, 0, 1000, 600), black_pen, gray_brush)

        # Rounded black board background
        path = QPainterPath()
        path.addRoundedRect(QRectF(10, 139, 980, 309), 75, 75)
        self.scene.addPath(path, black_pen, board_brush)

        # Stores
        self.scene.addEllipse(QRectF(27, 178, 120, 220), black_pen, white_brush)     # Left (AI)
        self.scene.addEllipse(QRectF(847, 178, 120, 220), black_pen, white_brush)    # Right (Player)

        # Pits (6 top row for AI, 6 bottom row for Player)
        for i in range(6):
            x = 147 + i * 119
            self.scene.addEllipse(QRectF(x, 183, 105, 105), black_pen, white_brush)  # AI row (top)
            self.scene.addEllipse(QRectF(x, 293, 105, 105), black_pen, white_brush)  # Player row (bottom)

        # "Your Turn" label
        turn_label = self.scene.addText("Your Turn", QFont("Arial", 16, QFont.Weight.Bold))
        turn_label.setDefaultTextColor(Qt.GlobalColor.red)
        turn_label.setPos(450, 110)

        # Score labels
        ai_score = self.scene.addText("AI Score: ${AiScore}", QFont("Arial", 14))
        ai_score.setPos(80, 470)

        player_score = self.scene.addText("Your Score: ${PlayerScore}", QFont("Arial", 14))
        player_score.setPos(780, 470)

    def create_rounded_rect(self,x1, y1, x2, y2, r=75, **kwargs):
        # Draw four arcs (corners)
        pass

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