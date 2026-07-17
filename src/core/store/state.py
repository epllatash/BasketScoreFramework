from dataclasses import dataclass


@dataclass
class GameState:

	# Equipos
	local_team: str = "LOCAL"
	visitor_team: str = "VISITANTE"

	# Marcador
	local_score: int = 0
	visitor_score: int = 0

	# Tiempo
	period: int = 1
	game_clock: str = "10:00"
	shot_clock: int = 24

	# Faltas
	local_fouls: int = 0
	visitor_fouls: int = 0

	# Tiempos muertos
	local_timeouts: int = 5
	visitor_timeouts: int = 5

	# Estado
	running: bool = False

