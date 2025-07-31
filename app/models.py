from datetime import datetime, timedelta
from app import db

# USER MODEL
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Reverse relationships: user.loans
    loans = db.relationship("Loan", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.name}>"
    
# BOOK MODEL
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    # Reverse relationship: book.loans
    loans = db.relationship("Loan", backref="book", lazy=True)

    def __repr__(self):
        return f"<Book {self.title}>"
    
# LOAN MODEL
class Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)

    borrowed_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime)
    returned_date = db.Column(db.DateTime, nullable=True)

    def __init__(self, user_id, book_id):
        self.user_id = user_id
        self.book_id = book_id
        self.borrowed_date = datetime.utcnow()
        self.due_date = self.borrowed_date + timedelta(days=14)

    def is_overdue(self):
        if self.returned_date:
            return self.returned_date > self.due_date
        return datetime.utcnow() > self.due_date
    
    def late_days(self):
        if self.returned_date:
            delta = self.returned_date - self.due_date
        else:
            delta = datetime.utcnow() - self.due_date
        return max(delta.days, 0)
    
    def late_fee(self):
        return self.late_days() * 0.25
    
    def __repr__(self):
        return f"<Loan Book {self.book_id} by User {self.user_id}"