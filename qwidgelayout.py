from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout

class MyWindow(QWidget):
    def init(self):
        super().init()

        # Create a vertical box layout
        layout = QVBoxLayout()

        # Create buttons
        btn1 = QPushButton("btn1")
        btn2 = QPushButton("btn2")
        btn3 = QPushButton("btn3")
        btn4 = QPushButton("btn4")

        # Add buttons to the layout
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)

        # Set the layout for the QWidget
        self.setLayout(layout)

# Create an instance of QApplication
app = QApplication([])

# Create an instance of MyWindow
window = MyWindow()
window.show()

# Execute the application's main loop
app.exec_()