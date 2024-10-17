from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QTextEdit, QPushButton, QDateEdit
)
from PyQt5.QtCore import QDate

class ProfileForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Profil Mahasiswa")
        self.setGeometry(100, 100, 400, 400)  # Mengatur ukuran jendela

        # Layout utama
        main_layout = QVBoxLayout()

        # Fungsi untuk membuat baris input
        def create_input_row(label_text):
            layout = QHBoxLayout()
            label = QLabel(label_text)
            input_field = QLineEdit()
            layout.addWidget(label)
            layout.addWidget(input_field)
            return layout, input_field

        # Baris input
        layout_nim, self.input_nim = create_input_row("NIM:")
        layout_nama, self.input_nama = create_input_row("Nama:")
        layout_kelas, self.input_kelas = create_input_row("Kelas:")
        layout_tempat_lahir, self.input_tempat_lahir = create_input_row("Tempat Lahir:")

        # Input Tanggal Lahir (menggunakan QDateEdit untuk kalender)
        layout_tanggal_lahir = QHBoxLayout()
        label_tanggal_lahir = QLabel("Tanggal Lahir:")
        self.input_tanggal_lahir = QDateEdit()
        self.input_tanggal_lahir.setCalendarPopup(True)
        self.input_tanggal_lahir.setDate(QDate.currentDate())
        layout_tanggal_lahir.addWidget(label_tanggal_lahir)
        layout_tanggal_lahir.addWidget(self.input_tanggal_lahir)

        # Baris input Telepon
        layout_telepon, self.input_telepon = create_input_row("Telepon:")

        # Input Alamat (menggunakan QTextEdit untuk teks panjang)
        layout_alamat = QHBoxLayout()
        label_alamat = QLabel("Alamat:")
        self.input_alamat = QTextEdit()
        layout_alamat.addWidget(label_alamat)
        layout_alamat.addWidget(self.input_alamat)

        # Baris tombol
        button_layout = QHBoxLayout()
        btn_simpan = QPushButton("Simpan")
        btn_edit = QPushButton("Edit")
        btn_hapus = QPushButton("Hapus")
        btn_batal = QPushButton("Batal")

        # Tambahkan tombol ke layout
        button_layout.addWidget(btn_simpan)
        button_layout.addWidget(btn_edit)
        button_layout.addWidget(btn_hapus)
        button_layout.addWidget(btn_batal)

        # Tambahkan semua layout ke layout utama
        main_layout.addLayout(layout_nim)
        main_layout.addLayout(layout_nama)
        main_layout.addLayout(layout_kelas)
        main_layout.addLayout(layout_tempat_lahir)
        main_layout.addLayout(layout_tanggal_lahir)
        main_layout.addLayout(layout_telepon)
        main_layout.addLayout(layout_alamat)
        main_layout.addLayout(button_layout)

        # Set layout utama ke jendela
        self.setLayout(main_layout)

# Inisialisasi aplikasi
app = QApplication([])
window = ProfileForm()
window.show()
app.exec_()
