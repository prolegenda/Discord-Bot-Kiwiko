from fastapi import FastAPI

app = FastAPI(title="HelixBot Dashboard API")


@app.get("/healthz")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
