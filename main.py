from kalah import Kalah
import sys
from PyQt6.QtWidgets import QApplication
from ui import KalahUI


game = Kalah()  # Initialize the Kalah game instance
app = QApplication(sys.argv)
window = KalahUI(game) 
window.show() 
sys.exit(app.exec())  