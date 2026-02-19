from helixbot.core.command_router import CommandRouter
from helixbot.core.di_container import Container
from helixbot.core.event_bus import EventBus
from helixbot.core.permissions import PermissionEngine
from helixbot.core.plugin_loader import PluginLoader
from helixbot.core.shard_manager import ShardManager


class HelixBotCore:
    def __init__(self) -> None:
        self.container = Container()
        self.event_bus = EventBus()
        self.permissions = PermissionEngine()
        self.command_router = CommandRouter()
        self.plugin_loader = PluginLoader()
        self.shard_manager = ShardManager()

    def bootstrap(self) -> None:
        self.container.register_singleton("event_bus", self.event_bus)
        self.container.register_singleton("permissions", self.permissions)
        self.container.register_singleton("command_router", self.command_router)
        self.container.register_singleton("plugin_loader", self.plugin_loader)
