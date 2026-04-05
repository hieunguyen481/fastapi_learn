from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Lesson 02"}


@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}


@app.get("/search")
def search(keyword: str):
    return {"keyword": keyword}


@app.get("/courses/{course_name}")
def get_course(course_name: str, level: str):
    return {
        "course_name": course_name,
        "level": level,
    }

@app.get("/filter/{filter_type}")
def get_filter(filter_type: str, value: str):
    return {
        "filter_type": filter_type,
        "value": value,
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User ID is {user_id}"
        }
