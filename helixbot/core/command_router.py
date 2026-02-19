from collections.abc import Awaitable, Callable

CommandHandler = Callable[[list[str]], Awaitable[None]]


class CommandRouter:
    def __init__(self) -> None:
        self._commands: dict[str, CommandHandler] = {}

    def register(self, name: str, handler: CommandHandler) -> None:
        self._commands[name] = handler

    async def execute(self, raw_content: str) -> bool:
        parts = raw_content.strip().split()
        if not parts:
            return False
        command = parts[0].lstrip("/")
        handler = self._commands.get(command)
        if handler is None:
            return False
        await handler(parts[1:])
        return True
