# 📚 Local Library Returns Tracker API

A lightweight Flask REST API that helps small, local libraries track borrowed books, return dates, and overdue fees. Built for learning, business realism, and professional portfolio showcase.

---

![Python](https://img.shields.io/badge/python-3.11-blue)
![Flask](https://img.shields.io/badge/flask-2.3-lightgrey)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

📦 [requirements.txt](./requirements.txt)  
🏃 [run.py](./run.py)

---

## ⚙️ Features

- 📖 Add and manage books
- 👤 Register library users
- 📆 Track borrow and return dates
- 🕒 Calculate overdue books and late fees ($0.25/day)
- 🔐 JWT login authentication
- 📃 Pagination for loan history
- 🧪 Fully tested with Pytest (JWT + business logic)
- 🧠 Future-ready: Email reminders, Swagger docs, and frontend integrations

---

## 🏗️ Tech Stack

| Tool        | Purpose                   |
|-------------|---------------------------|
| Flask       | Web API framework         |
| SQLAlchemy  | ORM for SQLite DB         |
| Marshmallow | Schema + serialization    |
| Pytest      | Automated testing         |
| JWT (Flask-JWT-Extended) | Auth system  |
| SQLite      | Lightweight local database|

---

## 🚀 Setup Instructions

### ✅ Prerequisites
- Python 3.11+
- Conda (recommended)

### 📦 Step 1: Create Environment

```bash
conda create -n library-api python=3.11
conda activate library-api
pip install -r requirements.txt
```
### 📦 Step 2: Initialize the Database

```
python seed_db.py
```

### 📦 Step 3: Run the API
```
python run.py
```
- visit http://localhost:5000 if using Windows
- On macOS, port 5000 is often reserved for AirPlay. To avoid conflicts, change the Flask port to 5050 in run.py

---

## 🔑 API Endpoints (Sample)

### 🔐 Auth
| Method | Route         | Description                   |
| ------ | ------------- | ----------------------------- |
| POST   | `/auth/login` | Log in via email, returns JWT |

### 👤 Users
| Method | Route         | Description     |
| ------ | ------------- | --------------- |
| GET    | `/users/`     | List all users  |
| POST   | `/users/`     | Create new user |
| DELETE | `/users/<id>` | Delete user     |

### 📖 Books
| Method | Route         | Description    |
| ------ | ------------- | -------------- |
| GET    | `/books/`     | List all books |
| POST   | `/books/`     | Add a book     |
| DELETE | `/books/<id>` | Remove a book  |

### 📘 Loans
| Method | Route                | Description                         |
| ------ | -------------------- | ----------------------------------- |
| POST   | `/loans/borrow`      | Borrow a book (JWT required)        |
| PUT    | `/loans/<id>/return` | Return a book (not implemented yet) |
| GET    | `/loans/overdue`     | List overdue books                  |
| GET    | `/loans/`            | Paginated loan list                 |

---

## 🧪 Testing Instructions
- Run all tests:
```
python -m pytest -s
```

✔️ Tests includes:
1. JWT login returns a valid token
2. Book borrowing logic (availability, due date)
3. Overdue endpoint shows empty list initially
Test setup uses an in-memory SQLite database with test fixtures in conftest.py.

---

## 🧠 Business Use Case

Many small libraries still use paper systems or spreadsheets to manage loans. This project simulates a modern backend that tracks:

- Borrowed books and due dates
- Automatically identifies overdue returns
- Computes late fees for library enforcement
- Built to mirror real-world backend design problems in a simple, clean structure.

---

## 💡 Future Plans

✅ Add book return route (PUT /loans/<id>/return)
📨 Add email reminder script (see email_reminder_logic.py)
🧾 Swagger/OpenAPI docs with Flasgger
🐳 Optional Docker container for deployment
🖥️ Frontend integration (Streamlit or React)

---

## 📂 Folder Structure
```
library-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── auth.py
│       ├── books.py
│       ├── loans.py
│       └── users.py
│
├── run.py
├── seed_db.py
├── config.py
├── requirements.txt
├── email_reminder_logic.py
├── pytest.ini
│
├── instance/
│   └── library.db
│
├── tests/
│   ├── conftest.py
│   └── test_app.py
```
---

## 🧑‍💻 Author

Sunil Makkar — backend developer in training, focused on real-world Python APIs and full-stack readiness.

---

## MIT License

Copyright (c) 2025 Sunil Makkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell   
copies of the Software, and to permit persons to whom the Software is        
furnished to do so, subject to the following conditions:                     

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.                              

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR   
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,     
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER       
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN    
THE SOFTWARE.
