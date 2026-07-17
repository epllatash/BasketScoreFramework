from src.core.store.store import game_store
from src.core.store.actions import (
    ADD_LOCAL_SCORE,
    ADD_VISITOR_SCORE,
)

from src.services.game_clock import game_clock


class GameController:

    def add_local_score(self, points: int):

        game_store.dispatch(
            ADD_LOCAL_SCORE,
            points
        )

    def add_visitor_score(self, points: int):

        game_store.dispatch(
            ADD_VISITOR_SCORE,
            points
        )

    def start_game(self):

        game_clock.start()

    def stop_game(self):

        game_clock.stop()

    def reset_game(self):

        game_clock.reset()


game_controller = GameController()
