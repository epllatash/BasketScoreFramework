from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BasketScore Framework")
        self.resize(1200, 700)

        central = QWidget()
        layout = QVBoxLayout()

        title = QLabel("🏀 BasketScore Framework")
        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)

        layout.addWidget(title)

        central.setLayout(layout)

        self.setCentralWidget(central)
