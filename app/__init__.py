from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)
    ma.init_app(app)

    # Import and register blueprints I will use later
    from app.routes.users import users_bp
    from app.routes.books import books_bp
    from app.routes.loans import loans_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(users_bp, url_prefix="/users")
    app.register_blueprint(books_bp, url_prefix="/books")
    app.register_blueprint(loans_bp, url_prefix="/loans")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app