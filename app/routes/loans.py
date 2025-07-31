from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import Loan, Book
from app.schemas import LoanSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

loans_bp = Blueprint("loans", __name__)

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)

# GET all books
from app.schemas import loans_schema

@loans_bp.route("/", methods=["GET"])
def get_loans():
    page = request.args.get("page", default=1, type=int)
    per_page = request.args.get("per_page", default=5, type=int)

    paginated_loans = Loan.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total_loans": paginated_loans.total,
        "total_pages": paginated_loans.pages,
        "current_page": paginated_loans.page,
        "per_page": paginated_loans.per_page,
        "loans": loans_schema.dump(paginated_loans.items)
    })

# POST - borrow book
@loans_bp.route("/borrow", methods=["POST"])
@jwt_required()
def book_book():
    user_id = get_jwt_identity()
    
    data = request.get_json()
    book_id = data.get("book_id")

    if not book_id:
        return jsonify({"error": "book_id is required"}), 400

    book = Book.query.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if not book.is_available:
        return jsonify({"error": "Book is currently unavailable"}), 400

    loan = Loan(user_id=user_id, book_id=book_id)
    book.is_available = False

    db.session.add(loan)
    db.session.commit()

    return loan_schema.jsonify(loan), 201

# GET - overdue books
@loans_bp.route("/overdue", methods=["GET"])
def get_overdue_loans():
    overdue_loans = Loan.query.filter(
        Loan.returned_date.is_(None),
        Loan.due_date < datetime.utcnow()
    ).all()

    return loans_schema.jsonify(overdue_loans)

