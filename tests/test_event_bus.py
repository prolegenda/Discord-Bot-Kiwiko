import asyncio

from helixbot.core.event_bus import EventBus


async def _run_test() -> None:
    bus = EventBus()
    received: list[int] = []

    async def handler(payload: dict[str, int]) -> None:
        received.append(payload["value"])

    bus.subscribe("metric", handler)
    await bus.emit("metric", {"value": 7})

    assert received == [7]


def test_event_bus_emit() -> None:
    asyncio.run(_run_test())
