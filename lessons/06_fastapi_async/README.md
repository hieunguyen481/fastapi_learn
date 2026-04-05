# Bài 6 - Dùng async trong FastAPI

## Mục tiêu
- Biết route sync và route async khác nhau thế nào
- Biết lỗi phổ biến: `async def` nhưng bên trong vẫn code block

## Kiến thức mới
- `async def` trong route
- `await asyncio.sleep()`
- phân biệt `time.sleep()` và `asyncio.sleep()`

## Giải thích quan trọng
- `time.sleep(3)` sẽ chặn chương trình 3 giây
- `await asyncio.sleep(3)` là chờ kiểu async

Nếu bạn viết `async def` nhưng bên trong dùng `time.sleep()`, route đó vẫn block.

## Cách chạy

```bash
uvicorn main:app --reload
```

## URL cần thử
- `/sync`
- `/async`
- `/bad`

## Bài tập tự làm
1. Tạo route `/slow` chờ 5 giây bằng async
2. Tạo route `/profile` trả JSON đơn giản nhưng viết theo kiểu sync
3. Tự giải thích vì sao `/bad` là ví dụ không nên làm
