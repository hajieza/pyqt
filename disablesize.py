from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QLabel, QDesktopWidget

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel(self)
        self.label.setText("Label1")
        self.label.move(200, 0)

        self.button = QPushButton(self)
        self.button.setText("Button1")
        self.button.move(0, 100)

        self.setGeometry(0, 0, 500, 500)
        self.setWindowTitle("Belajar PyQt5")
        
        # cek ukuran main window app kita
        cwa = self.frameGeometry()  
        cwc = QDesktopWidget().availableGeometry().center()  # posisi tengah layar
        self.move(cwa.topLeft())  
        self.setFixedSize(500, 500)  # Agar tidak bisa di-resize! icon maximize juga akan otomatis hilang

app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
