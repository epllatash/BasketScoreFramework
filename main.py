import sys

from PyQt6.QtWidgets import QApplication

from src.core.logging.logger import app_logger
from src.core.events.event_bus import event_bus
from src.core.events.events import GAME_STARTED
from src.presentation.windows.main_window import MainWindow


def main():
    app_logger.info("Iniciando BasketScore Framework...")

    event_bus.publish(GAME_STARTED)

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
