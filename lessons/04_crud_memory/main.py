from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Student(BaseModel):
    name: str
    age: int
    major: str


students = []


@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())
    return {"message": "Student added", "students": students}


@app.get("/students")
def get_students():
    return {"students": students}


@app.get("/students/{index}")
def get_student(index: int):
    if index < 0 or index >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    return students[index]


@app.put("/students/{index}")
def update_student(index: int, student: Student):
    if index < 0 or index >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    students[index] = student.model_dump()
    return {"message": "Student updated", "student": students[index]}


@app.delete("/students/{index}")
def delete_student(index: int):
    if index < 0 or index >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")
    deleted_student = students.pop(index)
    return {"message": "Student deleted", "student": deleted_student}
