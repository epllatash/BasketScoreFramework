
import sys

from PyQt6.QtWidgets import QApplication

from src.core.logging.logger import app_logger
from src.presentation.windows.main_window import MainWindow


def main():
	app_logger.info("Iniciando BasketScore Framework...")

	app = QApplication(sys.argv)

	window = MainWindow()
	window.show()

	sys.exit(app.exec())


if __name__ == "__main__":
	main()
