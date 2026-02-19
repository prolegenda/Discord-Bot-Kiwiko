from collections.abc import Callable
from typing import Any


class Container:
    def __init__(self) -> None:
        self._factories: dict[str, Callable[["Container"], Any]] = {}
        self._singletons: dict[str, Any] = {}

    def register_factory(self, key: str, factory: Callable[["Container"], Any]) -> None:
        self._factories[key] = factory

    def register_singleton(self, key: str, instance: Any) -> None:
        self._singletons[key] = instance

    def resolve(self, key: str) -> Any:
        if key in self._singletons:
            return self._singletons[key]
        if key in self._factories:
            instance = self._factories[key](self)
            self._singletons[key] = instance
            return instance
        raise KeyError(f"Service '{key}' is not registered")
