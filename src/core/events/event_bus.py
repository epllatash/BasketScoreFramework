from collections import defaultdict
from typing import Callable

from src.core.events.event import Event


class EventBus:

	def __init__(self):
		self._listeners = defaultdict(list)

	def subscribe(self, event_name: str, callback: Callable):

		self._listeners[event_name].append(callback)

	def publish(self, event_name: str, data=None):

		event = Event(event_name, data)

		for callback in self._listeners[event_name]:
			callback(event)


event_bus = EventBus()
