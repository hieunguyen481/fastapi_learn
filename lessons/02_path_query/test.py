from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {"message": "Lesson 02"}
# Path parameter
@app.get("/students")
def get_student(student_id: int):
    return {"student_id": student_id}
# Query parameter
@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}

# Kết hợp path parameter và query parameter
@app.get("/courses/{course_name}")
def get_course(course_name: str, lever: str):
    return {
        "course_name": course_name,
        "lever": lever,
    }
