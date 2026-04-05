from fastapi import FastAPI
from pydantic import BaseModel
import asyncio

app = FastAPI()

lectures = []


class Lecture(BaseModel):
    title: str
    content: str


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Lecture Assistant API"}


@app.post("/lectures")
def create_lecture(lecture: Lecture):
    lectures.append(lecture.model_dump())
    return {"message": "Lecture added", "lecture": lecture}


@app.get("/lectures")
def get_lectures():
    return {"lectures": lectures}


async def search_lecture(question: str):
    await asyncio.sleep(1)
    if lectures:
        return lectures[0]
    return None


async def create_answer(question: str, lecture):
    await asyncio.sleep(1)
    if lecture:
        return f"Cau tra loi cho '{question}' dua tren bai giang '{lecture['title']}'"
    return "Khong tim thay bai giang phu hop"


@app.post("/ask")
async def ask(data: QuestionRequest):
    lecture = await search_lecture(data.question)
    answer = await create_answer(data.question, lecture)

    return {
        "question": data.question,
        "matched_lecture": lecture,
        "answer": answer,
    }
