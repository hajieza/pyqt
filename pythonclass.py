from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel

# Define a custom main window class
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Initialize the parent QMainWindow
        self.label = QLabel(self)  # Create a label widget
        self.label.setText("Label1")  # Set label text
        self.label.move(200, 0)  # Move the label to position (200, 0)

        self.button = QPushButton(self)  # Create a button widget
        self.button.setText("Button1")  # Set button text

# Initialize the application
app = QApplication([])

# Create an instance of the custom window
window = MyWindow()

# Show the window
window.show()

# Start the application's event loop
app.exec_()
