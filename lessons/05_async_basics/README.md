# Bài 5 - Async cơ bản với asyncio

## Mục tiêu
- Hiểu `async def` là gì
- Hiểu `await` là gì
- Biết chạy hàm bất đồng bộ bằng `asyncio.run`

## Giải thích cực ngắn
`async` phù hợp khi chương trình phải **chờ** một việc nào đó, ví dụ:
- chờ mạng
- chờ API ngoài
- chờ database

Trong lúc chờ, chương trình có thể làm việc khác.

## Kiến thức mới
- `async def`
- `await`
- `asyncio.sleep()`
- `asyncio.run()`

## Cách chạy

```bash
python async_demo.py
```

## Điều cần quan sát
- Dòng `Start` in ra trước
- Chương trình chờ 2 giây
- Dòng `End` in ra sau

## Bài tập tự làm
1. Tạo hàm `say_bye()` chờ 1 giây rồi in `Bye`
2. Tạo hàm `task_a()` và `task_b()` rồi gọi tuần tự
3. Thử đổi thời gian sleep và quan sát kết quả
