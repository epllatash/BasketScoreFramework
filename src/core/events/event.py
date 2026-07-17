from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Event:
    name: str
    data: Any = None
    timestamp: datetime = datetime.now()
