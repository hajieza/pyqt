# ============ Menggunakan QMainWindow ======================
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

# Initialize the application
app = QApplication([])

# Create the main window
window = QMainWindow()

# Add a label (Using approach 2)
label = QLabel(window)  # cara 2
label.setText("Label1")  # Set label text
label.move(200, 0)       # Set label position

# Add a button (Using approach 2)
button = QPushButton(window)  # cara 2
button.setText("Button1")      # Set button text

# Show the window
window.show()

# Execute the application's event loop
app.exec_()
