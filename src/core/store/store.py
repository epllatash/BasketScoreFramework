from src.core.store.state import GameState
from src.core.store.reducer import reducer

from src.core.events.event_bus import event_bus
from src.core.events.score_events import (
    LOCAL_SCORE_CHANGED,
    VISITOR_SCORE_CHANGED
)

from src.core.store.actions import (
    ADD_LOCAL_SCORE,
    ADD_VISITOR_SCORE
)


class Store:

    def __init__(self):

        self.state = GameState()

        event_bus.subscribe(
            LOCAL_SCORE_CHANGED,
            self.local_score_changed
        )

        event_bus.subscribe(
            VISITOR_SCORE_CHANGED,
            self.visitor_score_changed
        )


    def dispatch(self, action, value=None):

        self.state = reducer(
            self.state,
            action,
            value
        )

        return self.state


    def local_score_changed(self, event):

        self.dispatch(
            ADD_LOCAL_SCORE,
            event.data
        )


    def visitor_score_changed(self, event):

        self.dispatch(
            ADD_VISITOR_SCORE,
            event.data
        )


game_store = Store()