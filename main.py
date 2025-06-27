from kalah import Kalah
import sys
from PyQt6.QtWidgets import QApplication
from ui import KalahUI


game = Kalah()  # Initialize the Kalah game instance
app = QApplication(sys.argv)
window = KalahUI(game)  # Initialize the UI with the game instance
window.show()  # Show the main window
sys.exit(app.exec())  # Start the application event loop