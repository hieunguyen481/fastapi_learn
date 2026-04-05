# Bài 1 - Hello World với FastAPI

## Mục tiêu
- Biết FastAPI là gì
- Biết tạo route đầu tiên
- Biết chạy server bằng Uvicorn
- Biết mở `/docs` để test API

## Kiến thức mới
- `FastAPI()`
- `@app.get()`
- JSON response
- `uvicorn main:app --reload`

## Các bước làm

### Bước 1: Tạo file `main.py`
Bạn sẽ tạo một ứng dụng FastAPI rất nhỏ.

### Bước 2: Viết route đầu tiên
Route là đường dẫn mà trình duyệt hoặc client gọi vào.

### Bước 3: Chạy server
Dùng Uvicorn để chạy ứng dụng.

### Bước 4: Mở docs
FastAPI tự sinh docs tại `/docs`.

## Cách chạy

```bash
uvicorn main:app --reload
```

## URL cần thử
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/docs`

## Giải thích code
- `from fastapi import FastAPI`: import framework
- `app = FastAPI()`: tạo ứng dụng
- `@app.get("/")`: khi có request GET đến `/`, chạy hàm bên dưới
- `return {"message": "Hello FastAPI"}`: trả JSON cho client

## Bài tập tự làm
1. Tạo route `/about`
2. Tạo route `/status`
3. Tạo route `/school` trả về tên trường
