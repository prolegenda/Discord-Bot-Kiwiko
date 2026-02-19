from dataclasses import dataclass
import os


@dataclass(slots=True)
class Settings:
    discord_token: str
    postgres_dsn: str
    redis_url: str
    shard_count: int = 1
    shards_per_process: int = 5

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            discord_token=os.getenv("DISCORD_TOKEN", ""),
            postgres_dsn=os.getenv("POSTGRES_DSN", "postgresql+asyncpg://localhost/helixbot"),
            redis_url=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
            shard_count=int(os.getenv("SHARD_COUNT", "1")),
            shards_per_process=int(os.getenv("SHARDS_PER_PROCESS", "5")),
        )
