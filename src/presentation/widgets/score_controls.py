from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from src.core.store.store import game_store
from src.core.store.actions import (
    ADD_LOCAL_SCORE,
    ADD_VISITOR_SCORE
)


class ScoreControls(QWidget):

    def __init__(self, refresh_callback):
        super().__init__()

        self.refresh_callback = refresh_callback

        layout = QVBoxLayout()


        local = QHBoxLayout()

        for points in [1, 2, 3]:

            button = QPushButton(
                f"Local +{points}"
            )

            button.clicked.connect(
                lambda checked,
                p=points:
                self.add_local(p)
            )

            local.addWidget(button)


        visitor = QHBoxLayout()

        for points in [1, 2, 3]:

            button = QPushButton(
                f"Visitante +{points}"
            )

            button.clicked.connect(
                lambda checked,
                p=points:
                self.add_visitor(p)
            )

            visitor.addWidget(button)


        layout.addLayout(local)
        layout.addLayout(visitor)

        self.setLayout(layout)


    def add_local(self, points):

        game_store.dispatch(
            ADD_LOCAL_SCORE,
            points
        )

        self.refresh_callback()


    def add_visitor(self, points):

        game_store.dispatch(
            ADD_VISITOR_SCORE,
            points
        )

        self.refresh_callback()
