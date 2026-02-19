from helixbot.core.bot import HelixBotCore
from helixbot.core.config import Settings


def create_app() -> HelixBotCore:
    settings = Settings.from_env()
    bot = HelixBotCore()
    bot.bootstrap()
    _ = settings
    return bot


if __name__ == "__main__":
    create_app()
