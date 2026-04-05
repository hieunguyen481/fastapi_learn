# fastapi_learn

Kho repo này được thiết kế cho người mới bắt đầu học **FastAPI** và **async** theo từng bài nhỏ, từ `Hello World` đến mini project.

Mục tiêu của repo:
- Học cách tạo API với FastAPI
- Hiểu `async` / `await` bằng ví dụ thật dễ
- Làm bài tập tăng dần độ khó
- Có sẵn cấu trúc để bạn lưu trữ lâu dài trên GitHub

## Repo này đang có gì?

```text
fastapi_learn/
├── .gitignore
├── requirements.txt
├── README.md
└── lessons/
    ├── 01_hello_world/
    ├── 02_path_query/
    ├── 03_post_pydantic/
    ├── 04_crud_memory/
    ├── 05_async_basics/
    ├── 06_fastapi_async/
    ├── 07_async_gather/
    ├── 08_async_httpx/
    └── 09_mini_project/
```

## Cài đặt môi trường

### 1. Tạo môi trường ảo

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Cài thư viện

```bash
pip install -r requirements.txt
```

## Cách chạy từng bài

Ví dụ với bài 1:

```bash
cd lessons/01_hello_world
uvicorn main:app --reload
```

Sau đó mở:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/docs

> Lưu ý: mỗi lần học một bài, bạn chỉ nên chạy trong đúng thư mục của bài đó.

## Lộ trình học đề xuất

### Giai đoạn 1 - Nền tảng FastAPI
1. `01_hello_world`: tạo API đầu tiên
2. `02_path_query`: path parameter và query parameter
3. `03_post_pydantic`: nhận JSON bằng POST và validate dữ liệu
4. `04_crud_memory`: CRUD cơ bản chưa dùng database

### Giai đoạn 2 - Async
5. `05_async_basics`: hiểu `async`, `await`, `asyncio.run`
6. `06_fastapi_async`: dùng async trong route FastAPI
7. `07_async_gather`: chạy nhiều tác vụ cùng lúc
8. `08_async_httpx`: gọi API ngoài bằng async

### Giai đoạn 3 - Ứng dụng gần project thật
9. `09_mini_project`: mini Lecture Assistant API

## Cách học hiệu quả nhất

Với mỗi bài:
1. Đọc `README.md` trong thư mục bài học
2. Tự gõ lại code, đừng chỉ copy
3. Chạy thử bằng `uvicorn`
4. Mở `/docs` để test
5. Tự sửa thêm 1-2 tính năng nhỏ
6. Làm phần “Bài tập tự làm”

## Những lệnh Git để đưa repo này lên GitHub

Vì repo GitHub của bạn hiện đang trống, bạn có thể dùng đúng các lệnh sau trong thư mục `fastapi_learn`:

```bash
git init
git branch -M main
git add .
git commit -m "Add FastAPI and async learning roadmap"
git remote add origin https://github.com/hieunguyen481/fastapi_learn.git
git push -u origin main
```

Nếu repo đã có remote rồi thì dùng:

```bash
git remote -v
```

Nếu cần đổi remote:

```bash
git remote remove origin
git remote add origin https://github.com/hieunguyen481/fastapi_learn.git
```

## Gợi ý commit message theo từng giai đoạn

- `Add lesson 01 hello world`
- `Add path and query parameter exercises`
- `Add POST and Pydantic examples`
- `Add CRUD in memory`
- `Add async basics exercises`
- `Add FastAPI async examples`
- `Add mini lecture assistant project`

## Mục tiêu cuối cùng sau repo này

Sau khi học xong, bạn nên làm được:
- Tự viết API CRUD cơ bản bằng FastAPI
- Hiểu khi nào dùng `async def`
- Phân biệt I/O-bound và CPU-bound
- Biết gọi API ngoài bằng async
- Biết tổ chức code backend nhỏ cho project AI hoặc web app
