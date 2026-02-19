from helixbot.core.shard_manager import ShardManager


def test_shard_allocation() -> None:
    manager = ShardManager()
    allocations = manager.allocate(shard_count=12, shards_per_process=5)
    assert [a.shard_ids for a in allocations] == [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11],
    ]
