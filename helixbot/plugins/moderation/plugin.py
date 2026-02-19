from helixbot.core.plugin_loader import BasePlugin


class Plugin(BasePlugin):
    name = "moderation"
    version = "0.1.0"
    dependencies = []

    async def setup(self, bot) -> None:
        return None

    async def teardown(self) -> None:
        return None
