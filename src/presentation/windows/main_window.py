from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

from src.core.store.store import game_store
from src.presentation.widgets.score_controls import ScoreControls
from src.core.events.event_bus import event_bus
from src.presentation.widgets.score_display import ScoreDisplayWidget

from src.core.events.score_events import (
    LOCAL_SCORE_CHANGED,
    VISITOR_SCORE_CHANGED
)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "BasketScore Framework"
        )

        self.resize(1200, 700)

        central = QWidget()

        layout = QVBoxLayout()


        title = QLabel(
            "🏀 BasketScore Framework"
        )

        title.setStyleSheet("""
            font-size:30px;
            font-weight:bold;
        """)


        self.score_display = ScoreDisplayWidget()

        layout.addWidget(self.score_display)


        self.score_display.refresh()

        event_bus.subscribe(
        LOCAL_SCORE_CHANGED,
        lambda event: self.update_score()
        )

        event_bus.subscribe(
        VISITOR_SCORE_CHANGED,
        lambda event: self.update_score()
        )
        controls = ScoreControls(
            self.update_score
        )


        layout.addWidget(title)
        layout.addWidget(controls)
        layout.addWidget(self.score_display)


        central.setLayout(layout)

        self.setCentralWidget(central)


    def update_score(self):
         self.score_display.refresh()