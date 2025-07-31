from app import create_app, db
from app.models import Loan, User, Book
from datetime import datetime

app = create_app()

def get_overdue_loans():
    with app.app_context():
        overdue_loans = Loan.query.filter(
            Loan.returned_date.is_(None),
            Loan.due_date < datetime.utcnow()
        ).all()

        if not overdue_loans:
            print("No overdue loans found.")
            return
        print("Sending remidners for {len(overdue_loans)} overdue loan(s)...\n")

        for loan in overdue_loans:
            user = User.query.get(loan.user_id)
            book = Book.query.get(loan.book_id)
            days_overdue = (datetime.utcnow() - loan.due_date).days
            late_fee = round(loan.late_fee(), 2)

            # Simulated email content
            message = f"""
Subject: Overdue Book Reminder

Hi {user.name},

This is a reminder that the book "{book.title}" by {book.author} is {days_overdue} day(s) overdue.

Please return it as soon as possible to avoid additional fees.

Current late fee: ${late_fee:.2f}

Thanks,
Your Local Library
"""
            print(message)
            print('=' * 60)

if __name__ == "__main__":
    get_overdue_loans()