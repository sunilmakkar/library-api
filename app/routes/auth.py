from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import User

auth_bp = Blueprint("auth", __name__)

# POST /auth/login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Invalid email"}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": access_token}), 200
