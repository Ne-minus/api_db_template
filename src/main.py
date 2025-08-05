import logging

import uvicorn
from fastapi import FastAPI

# from src.config import settings
from src.api.endpoints import router

logging.basicConfig(level=logging.INFO)


app = FastAPI()

app.include_router(router)


@app.get("/healthcheck")
def healthcheck():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
