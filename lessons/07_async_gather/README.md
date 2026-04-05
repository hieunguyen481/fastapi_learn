# Bài 7 - Chạy nhiều tác vụ cùng lúc với asyncio.gather

## Mục tiêu
- Hiểu vì sao async mạnh khi có nhiều tác vụ I/O
- Biết dùng `asyncio.gather()` để chạy đồng thời

## Giải thích
Nếu bạn gọi 2 tác vụ async theo kiểu tuần tự, thời gian sẽ cộng dồn.
Nhưng với `asyncio.gather()`, chúng có thể chạy gần như cùng lúc.

Ví dụ:
- task 1 mất 2 giây
- task 2 mất 3 giây

Tuần tự: khoảng 5 giây
Gộp bằng `gather`: khoảng 3 giây

## Cách chạy

```bash
python gather_demo.py
```

## Bài tập tự làm
1. Tạo thêm `fetch_data_3()` mất 1 giây
2. Thử chạy tuần tự rồi so sánh với `gather`
3. Đổi dữ liệu trả về thành dictionary
