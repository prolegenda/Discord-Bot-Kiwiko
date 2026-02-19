import asyncio
from collections.abc import Awaitable, Callable


class SchedulerService:
    def __init__(self) -> None:
        self._tasks: set[asyncio.Task] = set()

    def schedule(self, coro_factory: Callable[[], Awaitable[None]]) -> asyncio.Task:
        task = asyncio.create_task(coro_factory())
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)
        return task
