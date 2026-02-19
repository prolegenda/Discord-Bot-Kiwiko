import unittest

from helixbot.core.shard_manager import ShardManager


class ShardManagerTests(unittest.TestCase):
    def test_shard_allocation(self) -> None:
        manager = ShardManager()
        allocations = manager.allocate(shard_count=12, shards_per_process=5)
        self.assertEqual(
            [allocation.shard_ids for allocation in allocations],
            [
                [0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9],
                [10, 11],
            ],
        )


if __name__ == "__main__":
    unittest.main()
