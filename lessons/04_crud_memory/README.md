# Bài 4 - CRUD cơ bản bằng bộ nhớ RAM

## Mục tiêu
- Hiểu CRUD là gì
- Biết tạo, đọc, sửa, xóa dữ liệu bằng API
- Biết xử lý lỗi với `HTTPException`

## CRUD là gì?
- Create: tạo mới
- Read: đọc dữ liệu
- Update: cập nhật
- Delete: xóa

## Giải thích
Bài này chưa dùng database để bạn dễ tập trung vào luồng API.
Dữ liệu sẽ được lưu trong một list Python.

> Lưu ý: tắt server là mất dữ liệu.

## Route có trong bài
- `POST /students`
- `GET /students`
- `GET /students/{index}`
- `PUT /students/{index}`
- `DELETE /students/{index}`

## Cách chạy

```bash
uvicorn main:app --reload
```

## Bài tập tự làm
1. Tạo CRUD cho `Course`
2. Thêm field `email` cho `Student`
3. Tạo route đếm tổng số student
