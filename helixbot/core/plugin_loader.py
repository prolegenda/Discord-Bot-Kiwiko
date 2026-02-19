from dataclasses import dataclass
import importlib
from types import ModuleType
from typing import Any


class BasePlugin:
    name: str = "base"
    version: str = "0.0.0"
    dependencies: list[str] = []

    async def setup(self, bot: Any) -> None:
        return None

    async def teardown(self) -> None:
        return None


@dataclass(slots=True)
class LoadedPlugin:
    module: ModuleType
    instance: BasePlugin


class PluginLoader:
    def __init__(self) -> None:
        self._loaded: dict[str, LoadedPlugin] = {}

    @property
    def loaded(self) -> dict[str, LoadedPlugin]:
        return dict(self._loaded)

    async def load(self, dotted_path: str, bot: Any) -> BasePlugin:
        module = importlib.import_module(dotted_path)
        plugin_cls = getattr(module, "Plugin")
        plugin: BasePlugin = plugin_cls()
        for dependency in plugin.dependencies:
            if dependency not in self._loaded:
                raise RuntimeError(f"Missing plugin dependency: {dependency}")
        await plugin.setup(bot)
        self._loaded[plugin.name] = LoadedPlugin(module=module, instance=plugin)
        return plugin

    async def reload(self, name: str, bot: Any) -> BasePlugin:
        loaded = self._loaded[name]
        await loaded.instance.teardown()
        module = importlib.reload(loaded.module)
        plugin_cls = getattr(module, "Plugin")
        plugin: BasePlugin = plugin_cls()
        await plugin.setup(bot)
        self._loaded[name] = LoadedPlugin(module=module, instance=plugin)
        return plugin
