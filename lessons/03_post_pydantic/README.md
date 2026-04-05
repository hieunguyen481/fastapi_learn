# Bài 3 - POST request và Pydantic

## Mục tiêu
- Biết nhận dữ liệu JSON từ client
- Hiểu Pydantic dùng để validate dữ liệu
- Test POST trong `/docs`

## Kiến thức mới
- `BaseModel`
- `@app.post()`
- request body

## Giải thích
Khi client gửi JSON lên, FastAPI sẽ đọc JSON đó và kiểm tra xem có đúng cấu trúc mà bạn định nghĩa không.

Ví dụ model:
- `name`: chuỗi
- `age`: số nguyên
- `major`: chuỗi

Nếu client gửi sai kiểu dữ liệu, FastAPI sẽ báo lỗi rất rõ.

## Cách chạy

```bash
uvicorn main:app --reload
```

## JSON để test

```json
{
  "name": "Hieu",
  "age": 20,
  "major": "Computer Science"
}
```

## Bài tập tự làm
1. Tạo model `Course`
2. Tạo `POST /courses`
3. Thử gửi sai kiểu dữ liệu để xem FastAPI báo lỗi gì
