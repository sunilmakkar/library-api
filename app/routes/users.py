from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.schemas import UserSchema

users_bp = Blueprint("users", __name__)

user_schema = UserSchema()
users_schema = UserSchema(many=True)

# GET all users
@users_bp.route("/", methods=["GET"])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

# GET user by ID
@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return user_schema.jsonify(user)

# POST new user
@users_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()

    try:
        user = user_schema.load(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

# DELETE user by ID
@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"User {user.name} deleted."})