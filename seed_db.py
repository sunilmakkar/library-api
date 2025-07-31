from app import create_app, db
from app.models import User, Book

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create Users
    user1 = User(name="Alice Johnson", email="alice@example.com")
    user2 = User(name="Bob Smith", email="bob@example.com")
    user3 = User(name="John Kennedy", email="john@us.gov")
    user4 = User(name="Abe Lincoln", email="honestabe@example.com")
    user5 = User(name="Aubrey Graham", email="6ixgod@example.com")
    user6 = User(name="Tom Cruise", email="IDoMyOwnStunts@example.com")
    user7= User(name="Jimmy Stewart", email="OldJimbo@example.com")
    user8 = User(name="Vin Diesel", email="FamilyIsEverything@example.com")
    user9 = User(name="Barack Obama", email="pres@example.com")
    user10 = User(name="Shaquille O'Neal", email="superman@example.com")

    # Create Books
    book1 = Book(title="1984", author="George Orwell")
    book2 = Book(title="The Great Gatsby", author="F. Scott Fitzgerald")
    book3 = Book(title="To Kill a Mockingbird", author="Harper Lee")
    book4 = Book(title="I Know Why The Caged Bird Sings", author="Maya Angelou")
    book5 = Book(title="Legacy of Ashes", author="Tim Weiner")
    book6 = Book(title="Atomic Habits", author="James Clear")

    db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, book1, book2, book3, book4, book5, book6])
    db.session.commit()

    print("Database initialized and seeded with test data.")