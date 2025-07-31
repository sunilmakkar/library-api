from flask import Blueprint, request, jsonify
from app import db
from app.models import Book
from app.schemas import BookSchema

books_bp = Blueprint("books", __name__)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

# GET all books
@books_bp.route("/", methods=["GET"])
def get_books():
    books = Book.query.all()
    return books_schema.jsonify(books)

# GET book by ID
@books_bp.route("/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return book_schema.jsonify(book)

# POST new book
@books_bp.route("/", methods=["POST"])
def create_book():
    data = request.get_json()

    try:
        book = book_schema.load(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    db.session.add(book)
    db.session.commit()
    return book_schema.jsonify(book), 201

# DELETE book
@books_bp.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify({"message": f"Book '{book.title}' deleted."})
