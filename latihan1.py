from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contoh UI")

        # Membuat layout utama
        main_layout = QVBoxLayout()

        # Baris 1: Input NIM
        layout_nim = QHBoxLayout()
        label_nim = QLabel("NIM")
        self.input_nim = QLineEdit()
        layout_nim.addWidget(label_nim)
        layout_nim.addWidget(self.input_nim)

        # Baris 2: Input NAMA
        layout_nama = QHBoxLayout()
        label_nama = QLabel("NAMA")
        self.input_nama = QLineEdit()
        layout_nama.addWidget(label_nama)
        layout_nama.addWidget(self.input_nama)

        # Baris 3: Tombol
        layout_buttons = QHBoxLayout()
        button1 = QPushButton("PushButton1")
        button1.setStyleSheet("background-color: green; color: white;")
        button2 = QPushButton("PushButton2")
        button2.setStyleSheet("background-color: green; color: white;")
        layout_buttons.addWidget(button1)
        layout_buttons.addWidget(button2)

        # Tambahkan semua layout ke layout utama
        main_layout.addLayout(layout_nim)
        main_layout.addLayout(layout_nama)
        main_layout.addLayout(layout_buttons)

        # Set layout utama ke jendela
        self.setLayout(main_layout)

# Inisialisasi aplikasi
app = QApplication([])
window = MyWindow()
window.show()
app.exec_()
