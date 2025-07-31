import pytest
from app import create_app, db
from app.models import User, Book
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "JWT_SECRET_KEY": "test-secret"
    })

    with app.app_context():
        db.create_all()

        # Seed one user and book
        user = User(name="Test User", email="test@example.com")
        book = Book(title="Test Book", author="Author A")
        db.session.add_all([user, book])
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_token(app):
    with app.app_context():
        user = User.query.filter_by(email="test@example.com").first()
        return create_access_token(identity=str(user.id))

