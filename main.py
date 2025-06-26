import sys
from PyQt6.QtWidgets import QApplication
from ui import KalahUI

app = QApplication(sys.argv)
window = KalahUI()  # Initialize the UI with the game instance
window.show()  # Show the main window
sys.exit(app.exec())  # Start the application event loop