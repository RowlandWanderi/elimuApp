from models import db, User, TokenBlocklist
from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt



auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or request.form # Handle both JSON and form data
    email = data.get('email')  
    password = data.get('password')
    
    """ email = request.form.get("email")
    password = request.form.get("password")  """
    
    user = User.query.filter_by(email=email).first()

    if user:
        print(f"Debug: User Found - Email: {user.email}, Hashed Password: {user.password} {password}",)
        
        if check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id)
            return jsonify(access_token=access_token)
        
        print("Debug: Incorrect Password")
        return jsonify({f"error": "Wrong Password!"}), 401

    else:
        print(f"Debug: User Not Found Email: {email}")
        return jsonify({"error": "User doesn't exist!"}), 404
# Get logged in user
@auth_bp.route("/authenticated_user", methods=["GET"])
@jwt_required()
def authenticated_user():
    current_user_id = get_jwt_identity()  # getting current user id
    user = User.query.get(current_user_id)

    if user:
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
            
            
        }
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Logout user
@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    jwt = get_jwt()

    jti = jwt['jti']

    token_b = TokenBlocklist(jti=jti)
    db.session.add(token_b)
    db.session.commit()

    return jsonify({"success": "Logged out successfully!"}), 200


# Reset user password
@auth_bp.route("/reset_password", methods=["POST"])
def reset_password():
    data = request.get_json()
    email = data.get("email")
    new_password = data.get("new_password")

    user = User.query.filter_by(email=email).first()

    if user:
        # Hash the new password before storing it
        hashed_password = generate_password_hash(new_password)

        # Update the user's password
        user.password = hashed_password
        db.session.commit()

        return jsonify({"success": "Password reset successful"}), 200
    else:
        return jsonify({"error": "User with the provided email not found"}), 404
