# Bài 9 - Mini project: Lecture Assistant API

## Mục tiêu
Gom toàn bộ kiến thức đã học để làm một backend demo gần với project thật:
- thêm bài giảng
- xem danh sách bài giảng
- hỏi câu hỏi về bài giảng
- mô phỏng bước search và answer bằng async

## Bạn sẽ luyện gì trong bài này?
- `GET` và `POST`
- Pydantic model
- lưu dữ liệu trong RAM
- route async
- gọi nhiều hàm async theo luồng đơn giản

## Luồng của API
1. User gửi câu hỏi
2. Server tìm bài giảng liên quan
3. Server tạo câu trả lời dựa trên bài giảng đó
4. Trả kết quả về cho user

## Cách chạy

```bash
uvicorn main:app --reload
```

## Các route
- `GET /`
- `POST /lectures`
- `GET /lectures`
- `POST /ask`

## Gợi ý test
### 1. Thêm lecture

```json
{
  "title": "FastAPI Introduction",
  "content": "FastAPI is a modern Python framework for building APIs."
}
```

### 2. Gửi câu hỏi

```json
{
  "question": "FastAPI dung de lam gi?"
}
```

## Bài tập tự làm
1. Cho phép thêm nhiều lecture rồi tìm lecture gần đúng hơn
2. Trả về thêm `citation` giả lập
3. Tạo route `/summary` cho từng bài giảng
4. Tách code thành `models.py`, `services.py`, `main.py`
