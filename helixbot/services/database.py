class DatabaseService:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    async def connect(self) -> None:
        return None

    async def close(self) -> None:
        return None
