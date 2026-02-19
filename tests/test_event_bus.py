import asyncio
import unittest

from helixbot.core.event_bus import EventBus


class EventBusTests(unittest.TestCase):
    def test_event_bus_emit(self) -> None:
        async def run_test() -> list[int]:
            bus = EventBus()
            received: list[int] = []

            async def handler(payload: dict[str, int]) -> None:
                received.append(payload["value"])

            bus.subscribe("metric", handler)
            await bus.emit("metric", {"value": 7})
            return received

        received = asyncio.run(run_test())
        self.assertEqual(received, [7])


if __name__ == "__main__":
    unittest.main()
