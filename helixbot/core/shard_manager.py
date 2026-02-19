from dataclasses import dataclass


@dataclass(slots=True)
class ShardAllocation:
    process_index: int
    shard_ids: list[int]


class ShardManager:
    def allocate(self, shard_count: int, shards_per_process: int) -> list[ShardAllocation]:
        allocations: list[ShardAllocation] = []
        process_index = 0
        for start in range(0, shard_count, shards_per_process):
            shard_ids = list(range(start, min(start + shards_per_process, shard_count)))
            allocations.append(ShardAllocation(process_index=process_index, shard_ids=shard_ids))
            process_index += 1
        return allocations
