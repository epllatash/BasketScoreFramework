from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

from src.core.store.store import game_store
from src.presentation.widgets.score_controls import ScoreControls
from src.core.events.event_bus import event_bus

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


        self.score_label = QLabel()

        self.score_label.setStyleSheet("""
            font-size:50px;
            font-weight:bold;
        """)


        self.update_score()


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
        layout.addWidget(self.score_label)
        layout.addWidget(controls)


        central.setLayout(layout)

        self.setCentralWidget(central)


    def update_score(self):

        state = game_store.state

        self.score_label.setText(
            f"""
            {state.local_team}

            {state.local_score}

            -

            {state.visitor_score}

            {state.visitor_team}
            """
        )