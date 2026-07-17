from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

from src.core.store.store import game_store


class ScoreDisplayWidget(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.title = QLabel("MARCADOR")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.title.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
        """)

        self.score = QLabel()

        self.score.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.score.setStyleSheet("""
            font-size:70px;
            font-weight:bold;
        """)

        layout.addWidget(self.title)
        layout.addWidget(self.score)

        self.setLayout(layout)

        self.refresh()

    def refresh(self):

        state = game_store.state

        self.score.setText(
            f"{state.local_score}   -   {state.visitor_score}"
        )
