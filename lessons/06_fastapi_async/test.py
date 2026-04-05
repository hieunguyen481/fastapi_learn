import asyncio

from fastapi import FastAPI

import time

app=FastAPI()


@app.get("/sync")
def sync_route():
    time.sleep(3)
    return{"message":"sync done"}

@app.get("/async")
async def async_route():
    await asyncio.sleep(3)
    return{"message":"async done"}

@app.get("/bad")
async def bad_route():
    time.sleep(3)
    return {"message": "This route looks async but still blocks"}
