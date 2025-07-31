# 🧠 Project Deep Dive: Local Library Returns Tracker API

A detailed breakdown of how this REST API works under the hood. Designed for learning, interview prep, and long-term reference.

---

## 1. 🌐 Route-by-Route Breakdown

### `/auth/login`
- **Method**: `POST`
- **Purpose**: Authenticates a user and returns a JWT.
- **Flow**:
  1. User sends `email` via JSON.
  2. The route checks if the email exists in the DB.
  3. If valid, creates a JWT with `user.id` as identity.
  4. Returns `{ access_token: <token> }`.

---

### `/users/`
- **GET**: Lists all users from the database.
- **POST**: Creates a new user with `name` and `email`.
- **DELETE /users/<id>`**: Removes user by ID.

---

### `/books/`
- **GET**: Returns a list of all books.
- **POST**: Adds a new book (`title`, `author`).
- **DELETE /books/<id>`**: Removes book by ID.

---

### `/loans/borrow`
- **Method**: `POST`  
- **Protected**: Requires JWT
- **Flow**:
  1. Extracts `book_id` from JSON.
  2. Retrieves current user from token.
  3. Finds book in DB.
  4. Sets `borrowed_date = today`, `due_date = today + 14 days`.
  5. Creates a loan record.

---

### `/loans/`
- **GET**: Returns paginated list of all loans.

---

### `/loans/overdue`
- **GET**: Returns a list of overdue books.
- Logic:
  - A loan is overdue if `returned_date` is `None` **and** `due_date < today`.
  - Late fee = `(today - due_date).days * $0.25`.

---

## 2. 🧱 Models and Their Purpose

### `User`
- `id`, `name`, `email`
- Used for login and loan assignment.

### `Book`
- `id`, `title`, `author`
- Represents catalog items.

### `Loan`
- `id`, `user_id`, `book_id`, `borrowed_date`, `due_date`, `returned_date`
- Links users to books with timestamp logic.
- Two hybrid properties:
  - `is_overdue`: Boolean
  - `late_fee`: Computed fee if overdue

---

## 3. ⚙️ Key Business Logic

### Borrowing a Book
- Validates JWT.
- Ensures book exists.
- Ensures no duplicate active loan for same book.
- Creates and commits a new `Loan`.

---

### Overdue Calculation
- Done dynamically using Python’s `datetime`.
- A loan is overdue if `returned_date` is `None` and the current date is past the due date.
- Late fee calculated as `$0.25 * days overdue`.

---

### Returning a Book (Planned)
- Will update `returned_date` on an existing loan.
- Late fee check will then be static after return.

---

## 4. 🔐 JWT Flow

- **Login**: Issues JWT using `create_access_token(identity=user.id)`
- **Protected Routes**: Decorated with `@jwt_required()`
- **Usage**:
  - Client sends token in header:
    ```
    Authorization: Bearer <token>
    ```
  - Inside route, `user_id = get_jwt_identity()` retrieves the user.

---

## 5. 🧪 Testing System

### Pytest Setup
- Uses in-memory SQLite DB
- `conftest.py`:
  - `client()` fixture = API test client
  - `auth_token()` = JWT token for testing auth

### Tests in `test_app.py`
- ✅ Valid JWT returns
- ✅ Borrowing a book works
- ✅ Overdue detection logic
- Tests simulate real flows like borrowing and querying with pagination.

---

## 6. 💭 What I Learned

- How REST APIs really work behind the scenes
- How to design routes that map cleanly to real-world use cases
- JWT authentication in practice — not just theory
- Hybrid properties in SQLAlchemy are powerful for on-the-fly logic
- Testing with Pytest fixtures made my codebase testable and modular
- I now understand the API request-response lifecycle from login to borrowing to checking late fees

---

This file serves as a “second brain” for my API work — I’ll refer back to it as I continue building real-world backend tools.
