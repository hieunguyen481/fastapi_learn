from fastapi import FastAPI

app = FastAPI() # tạo ứng dụng FastAPI

@app.get("/") # khi co request GET đến / , chạy hàm dưới
def home():
    return {"message": "Hello FastAPI"} # trả về một dict có key là message và value là "Hello FastAPI" khi có request GET đến /

@app.get("/about") # khi co request GET đến /about , chạy hàm dưới
def about():
    return {"message": "This is lesson 01"} # trả về một dict có key là message và value là "This is lesson 01" khi có request GET đến /about