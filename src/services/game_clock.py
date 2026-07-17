from PyQt6.QtCore import QObject, QTimer, pyqtSignal


class GameClock(QObject):

    tick = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.seconds = 600  # 10 minutos

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)

    def start(self):
        self.timer.start(1000)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.seconds = 600
        self.tick.emit(self.format_time())

    def update_clock(self):

        if self.seconds > 0:
            self.seconds -= 1

        self.tick.emit(
            self.format_time()
        )

    def format_time(self):

        minutes = self.seconds // 60
        seconds = self.seconds % 60

        return f"{minutes:02}:{seconds:02}"


game_clock = GameClock()
