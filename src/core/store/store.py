from src.core.store.state import GameState
from src.core.store.reducer import reducer


class Store:

    def __init__(self):

        self.state = GameState()

    def dispatch(self, action, value=None):

        self.state = reducer(
            self.state,
            action,
            value
        )

        return self.state


game_store = Store()
