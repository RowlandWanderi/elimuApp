from models import db, User
from flask import request, jsonify, Blueprint
from flask_jwt_extended import  jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)


# Create a user
@user_bp.route("/register", methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = generate_password_hash(data.get("password"), )
    
    
    check_username = User.query.filter_by(username = username).first()
    check_email = User.query.filter_by(email = email).first()

    
    if check_username or check_email:
        conflicting_field = "username" if check_username else "email" 
        return jsonify({"error": f"{conflicting_field} already exists!"}), 409    
    else:
        new_user = User(email = email, password = password, username = username, )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success": "User added successfully!"}), 201
    
    
# Get details of a single user
@user_bp.route("/users/<int:id>")
def get_user(id):
    user = User.query.get(id)
    user_list =[]
    
    if user:
        user_list.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role,
        })
        return jsonify(user_list), 200
    else:
        return jsonify({"error": "User not found!"}), 404
    
    
# Update single user's details
@user_bp.route("/users", methods = ["PUT"])
@jwt_required()
def update_user():
    user = User.query.get(get_jwt_identity())
    data = request.get_json()
    
    if user:
        new_username = data.get('username', user.username)
        email = data.get('email', user.email)
        
        check_username = User.query.filter(User.id != get_jwt_identity(), User.username == new_username).first()
        check_email = User.query.filter(User.id != get_jwt_identity(), User.email == email).first()
        
        
        if check_username or check_email :
            return jsonify({"error": "User email/username"})

        else:
            user.username = new_username
            user.email = email

            
            db.session.commit()
            return jsonify({"success": f"{new_username} updated successfully"}), 200
        
    else:
        return jsonify({"error":"The user you are trying to update does not exist!"}), 404


# Delete User's account
@user_bp.route("/users", methods = ["DELETE"])
@jwt_required()
def delete_user():
    user = User.query.get(get_jwt_identity())
    
    if user:
        
            
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success": "User deleted successfully"}), 200
    else:
        return jsonify({"error": "The user you are trying to delete does not exist"}), 404