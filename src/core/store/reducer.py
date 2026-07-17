from src.core.store.actions import *
from src.core.store.state import GameState


def reducer(state: GameState, action: str, value=None):

    if action == ADD_LOCAL_SCORE:
        state.local_score += value

    elif action == ADD_VISITOR_SCORE:
        state.visitor_score += value

    elif action == RESET_GAME:
        state.local_score = 0
        state.visitor_score = 0
        state.period = 1
        state.game_clock = "10:00"

    elif action == START_GAME:
        state.running = True

    elif action == STOP_GAME:
        state.running = False

    return state
