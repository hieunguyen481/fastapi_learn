# Bài 2 - Path parameter và Query parameter

## Mục tiêu
- Hiểu cách lấy dữ liệu từ URL
- Phân biệt path parameter và query parameter

## Kiến thức mới
- `@app.get("/students/{student_id}")`
- query string như `?keyword=python`
- type hint `int`, `str`

## Giải thích dễ hiểu

### Path parameter
Là dữ liệu nằm ngay trong đường dẫn.
Ví dụ:

```text
/students/10
```

Ở đây `10` là `student_id`.

### Query parameter
Là dữ liệu nằm sau dấu `?`.
Ví dụ:

```text
/search?keyword=fastapi
```

Ở đây `keyword` là query parameter.

## Cách chạy

```bash
uvicorn main:app --reload
```

## URL cần thử
- `http://127.0.0.1:8000/students/5`
- `http://127.0.0.1:8000/search?keyword=async`
- `http://127.0.0.1:8000/courses/python?level=basic`

## Bài tập tự làm
1. Tạo route `/books/{book_id}`
2. Tạo route `/filter?topic=python`
3. Tạo route `/users/{user_id}` trả thêm một message mô tả
