from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/posts")
async def get_posts():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        data = response.json()[:5]
        return {"count": len(data), "posts": data}
