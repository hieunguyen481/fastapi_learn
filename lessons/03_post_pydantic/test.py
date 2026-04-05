from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Student(BaseModel):
    name:str
    age:int
    major:str

@app.post("/students")
def create_student(student:Student):
    return {
        "message": "Student created successflully", 
        "student": student,
    }
    
