from flask_marshmallow import Marshmallow
from app.models import User, Book, Loan

ma = Marshmallow()

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

# Book Schema
class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

# Loan Schema
class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loan
        load_instance = True
        include_fk = True

    # Add computed fields
    is_overdue = ma.Method("get_is_overdue")
    late_fee = ma.Method("get_late_fee")

    def get_is_overdue(self, obj):
        return obj.is_overdue()
    
    def get_late_fee(self, obj):
        return round(obj.late_fee(), 2) if obj.is_overdue() else 0.00
    
# Schema Instances
user_schema = UserSchema()
users_schema = UserSchema(many=True)

book_schema = BookSchema()
books_schema = BookSchema(many=True)

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)