import random
from fastapi import FastAPI
from asyncio import sleep
app = FastAPI()

@app.get("/instant")
async def instant():
    return {"message": "ok"}

@app.get("/wait")
async def wait():
    await sleep(2)
    return {"message": "ok"}

@app.get("/wait-random")
async def wait_random():
    time_to_wait = random.randint(1, 3)
    await sleep(time_to_wait)
    return {"message": "ok"}


