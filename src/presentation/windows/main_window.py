from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel
)

from src.core.store.store import game_store


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


        state = game_store.state


        marcador = QLabel(
            f"""
            {state.local_team}

            {state.local_score}

            -

            {state.visitor_score}

            {state.visitor_team}
            """
        )


        marcador.setStyleSheet("""
            font-size:50px;
            font-weight:bold;
        """)


        layout.addWidget(title)
        layout.addWidget(marcador)


        central.setLayout(layout)

        self.setCentralWidget(central)
