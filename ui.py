# User Interface for Kalah
from PyQt6.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsPixmapItem, QGraphicsEllipseItem, QGraphicsRectItem, QPushButton, QWidget, QGraphicsItemGroup
from PyQt6.QtGui import QBrush, QPen, QColor, QPainterPath, QFont, QPainter, QPixmap
from PyQt6.QtCore import QRectF,Qt, QTimer
import random
import os 
from games import GameState, alpha_beta_cutoff_search, alpha_beta_player

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

        board = self.state.board
        print(f"Current Board State: {board}")
        # Stores
        self.scene.addEllipse(QRectF(27, 178, 120, 220), black_pen, white_brush)     # Left (AI)
        self.scene.addEllipse(QRectF(847, 178, 120, 220), black_pen, white_brush)    # Right (Player)
        

        # Pits (6 top row for AI, 6 bottom row for Player)
        for i in range(6):
            x = 147 + i * 119
            self.scene.addEllipse(QRectF(x, 183, 105, 105), black_pen, white_brush)  # AI row (top)
            ellipse = QGraphicsEllipseItem(QRectF(x, 293, 105, 105))  # Player row (bottom)
            ellipse.setBrush(QBrush(Qt.GlobalColor.white))
            ellipse.setPen(black_pen)
            ellipse.setData(0, 5 - i)
            ellipse.setAcceptHoverEvents(True)
            ellipse.setFlag(QGraphicsPixmapItem.GraphicsItemFlag.ItemIsSelectable)
            ellipse.mousePressEvent = lambda event, pit_index= i: self.clickHandler(event,pit_index)
            self.scene.addItem(ellipse)



            # AI pits labels
            pit_label = self.scene.addText(f"{board[12 - i]}", QFont("Arial", 24))
            pit_label.setDefaultTextColor(Qt.GlobalColor.white)
            pit_label.setPos(187 + i * 119, 154)

            # Player pits labels
            pit_label = self.scene.addText(f"{board[i]}", QFont("Arial", 24))
            pit_label.setDefaultTextColor(Qt.GlobalColor.white)
            pit_label.setPos(187 + i * 119, 402)

        # Turn Label
        self.turn_label = self.scene.addText("Your Turn", QFont("Arial", 16, QFont.Weight.Bold))
        self.turn_label.setDefaultTextColor(Qt.GlobalColor.red)
        self.turn_label.setPos(459, 107)

        # Score labels
        ai_score = self.scene.addText(("AI Score: " + str(board[13])), QFont("Arial", 24))
        ai_score.setDefaultTextColor(Qt.GlobalColor.black)
        ai_score.setPos(76, 463)

        player_score = self.scene.addText(("Your Score: " + str(board[6])), QFont("Arial", 24))
        player_score.setDefaultTextColor(Qt.GlobalColor.black)
        player_score.setPos(795, 463)

        if self.stone_pixmaps:

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
                count = board[12 - i] 
                for _ in range(count):
                    x = random.randint((175 + i * 119),225 + i * 119)
                    y = random.randint(211, 261)
                    bead = QGraphicsPixmapItem(random.choice(self.stone_pixmaps))
                    bead.setPos(x, y)
                    self.scene.addItem(bead)

            # Player Pits
            for i in range(6):
                count = board[i]
                for _ in range(count):
                    x = random.randint((175 + i * 119),225 + i * 119)
                    y = random.randint(321, 371)
                    bead = QGraphicsPixmapItem(random.choice(self.stone_pixmaps))
                    bead.setPos(x, y)
                    self.scene.addItem(bead)
            
        else:
            print(f"No bead images found")

        reset_group = QGraphicsItemGroup()
        # --- Reset Button on Canvas ---
        reset_button_rect = QGraphicsRectItem(QRectF(440, 480, 120, 40))
        reset_button_rect.setBrush(QBrush(Qt.GlobalColor.gray))
        reset_button_rect.setPen(QPen(Qt.GlobalColor.black))
        reset_button_rect.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable)
        reset_button_rect.setCursor(Qt.CursorShape.PointingHandCursor)

        # Add text label over the rectangle
        reset_text = self.scene.addText("Reset Game", QFont("Arial", 12, QFont.Weight.Bold))
        reset_text.setDefaultTextColor(Qt.GlobalColor.black)
        reset_text.setPos(455, 485)

        # Group the button and label (optional)
  
        reset_group.addToGroup(reset_button_rect)
        reset_group.addToGroup(reset_text)

        # Add to scene
        self.scene.addItem(reset_group)


        # Assign event handler to reset button
        reset_group.mousePressEvent = lambda event: self.resetGame()

    def updateBoard(self): # updates pit counts, shows whose turn it is, etc.
        # two lists for pit labels and counts

        # fill according to state, maybe view the dropping of seeds and show that 
        pass 


    def clickHandler(self, event, pit_index): # determines which pit was clicked & validates 
        if self.state.to_move != 'MAX':
            print("Not your turn.")
            return

        legal_moves = self.game.actions(self.state)
        if pit_index not in legal_moves:
            print(f"Invalid move: {pit_index}")
            return

        print(f"You selected pit: {pit_index}")
        self.process_move(pit_index)

        if self.game.terminal_test(self.state):
            print("Game Over!")
            self.drawBoard()
            utility = self.game.utility(self.state, 'MAX')  # 'MAX' is the human player

            if self.state.board[6] > self.state.board[13]:
                self.turn_label.setPlainText("You win!")
            elif self.state.board[6] < self.state.board[13]:
                self.turn_label.setPlainText("AI wins!")
            else:
                self.turn_label.setPlainText("It's a tie!")

            return 
        
        self.drawBoard()

        if self.game.to_move(self.state) == 'MIN':
            self.handle_ai_turn()


    def process_move(self, move):
        self.state = self.game.result(self.state, move)
        self.drawBoard()

        if self.game.terminal_test(self.state):
            self.handle_game_end()
        elif self.state.to_move == 'MAX':
            self.turn_label.setPlainText("Your extra turn!")
        else:
            self.turn_label.setPlainText("AI's Turn")
            QTimer.singleShot(500, self.handle_ai_turn)

    def handle_ai_turn(self):
        while self.state.to_move == 'MIN' and not self.game.terminal_test(self.state):
            move = alpha_beta_player(self.game, self.state)
            if move is None:
                break
            print(f"AI chooses: {move}")
            self.state = self.game.result(self.state, move)
            self.drawBoard()

        if self.game.terminal_test(self.state):
            self.handle_game_end()
        elif self.state.to_move == 'MAX':
            self.turn_label.setPlainText("Your Turn")

    def handle_game_end(self):
        player_score = self.state.board[6]
        ai_score = self.state.board[13]
        result = self.game.utility(self.state, 'MAX')

        if result > 0:
            outcome = "You Win!"
        elif result < 0:
            outcome = "AI Wins!"
        else:
            outcome = "It's a Tie!"

        self.turn_label.setPlainText(f"Game Over — {outcome}")
        print(f"Final Score: You {player_score}, AI {ai_score}")

    def resetGame(self):
        board = [4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0]
        moves = [0,1,2,3,4,5]
        self.state = GameState(to_move='MAX',utility=0, moves=moves,board=board)        
        self.drawBoard()
        self.turn_label.setPlainText("Your Turn")

if __name__ == "__main__":

    ui = KalahUI()  # Initialize the UI with the game instance