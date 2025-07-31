from app.models import Book
from app import db

def test_logic_returns_token(client):
    response = client.post("/auth/login", json={"email": "test@example.com"})
    data = response.get_json()
    assert response.status_code == 200
    assert "access_token" in data

def test_borrow_book(client, auth_token):
    with client.application.app_context():
        book = Book.query.filter_by(title="Test Book").first()
    book_id = book.id

    headers = {"Authorization": f"Bearer {auth_token}"}
    response = client.post("/loans/borrow", json={"book_id": book_id}, headers=headers)
    data = response.get_json()
    print("[DEBUG] Response JSON:", data)

    assert response.status_code == 201
    assert data["book_id"] == book_id
    assert data["returned_date"] is None

def test_get_overdue_books_empty(client):
    response = client.get("/loans/overdue")
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 0

