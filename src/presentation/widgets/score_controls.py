from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout
)

from src.core.events.event_bus import event_bus
from src.core.events.score_events import (
    LOCAL_SCORE_CHANGED,
    VISITOR_SCORE_CHANGED
)


class ScoreControls(QWidget):

    def __init__(self, refresh_callback=None):

        super().__init__()

        self.refresh_callback = refresh_callback

        layout = QVBoxLayout()


        local_layout = QHBoxLayout()

        for points in [1, 2, 3]:

            button = QPushButton(
                f"Local +{points}"
            )

            button.clicked.connect(
                lambda _, p=points: self.add_local(p)
            )

            local_layout.addWidget(button)


        visitor_layout = QHBoxLayout()

        for points in [1, 2, 3]:

            button = QPushButton(
                f"Visitante +{points}"
            )

            button.clicked.connect(
                lambda _, p=points: self.add_visitor(p)
            )

            visitor_layout.addWidget(button)


        layout.addLayout(local_layout)
        layout.addLayout(visitor_layout)

        self.setLayout(layout)


    def add_local(self, points):

        print("CLICK LOCAL:", points)

        event_bus.publish(
            LOCAL_SCORE_CHANGED,
            points
        )


    def add_visitor(self, points):

        print("CLICK VISITANTE:", points)

        event_bus.publish(
            VISITOR_SCORE_CHANGED,
            points
        )