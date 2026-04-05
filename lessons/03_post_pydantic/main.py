from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    major: str

class Course(BaseModel):
    name: str
    level: int
    description: str


@app.post("/students")
def create_student(student: Student):
    return {
        "message": "Student created successfully",
        "student": student,
    }

@app.post("/courses")
def create_course(course: Course):
    return {
        "message": "Course created successfully",
        "course": course,
    }