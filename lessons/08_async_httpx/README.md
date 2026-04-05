# Bài 8 - Gọi API ngoài bằng async với httpx

## Mục tiêu
- Biết cách gọi API ngoài trong FastAPI
- Biết dùng `httpx.AsyncClient()`
- Hiểu đây là ví dụ I/O-bound rất điển hình

## Kiến thức mới
- `httpx.AsyncClient()`
- `await client.get(...)`

## Giải thích
Khi server của bạn gọi một API khác, nó phải chờ mạng phản hồi.
Đây là lúc `async` phát huy tác dụng rất mạnh.

## Cách chạy

```bash
uvicorn main:app --reload
```

## URL cần thử
- `/posts`

## Bài tập tự làm
1. Chỉ lấy 3 bài post đầu tiên
2. Trả về thêm tổng số lượng post lấy được
3. Thử đổi endpoint khác và xem phản hồi
