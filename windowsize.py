# ============ Window Management ===========================
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

# Define a custom main window class
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the QMainWindow parent class

        # Create and configure the label
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)  # Position the label at (200, 0)

        # Create and configure the button
        self.button = QPushButton(self)
        self.button.setText("Button1")  # Set the button text

        # Set window size and position: (x, y, width, height)
        self.setGeometry(0, 0, 400, 400)

        # Set the window title
        self.setWindowTitle("Belajar PyQt5")

# Initialize the application
app = QApplication([])

# Create an instance of the custom window
window = MyWindow()

# Show the window
window.show()

# Start the application's event loop
app.exec_()
