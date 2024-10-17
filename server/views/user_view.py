from models import db, User
from flask import request, jsonify, Blueprint
from flask_jwt_extended import  jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash

user_bp = Blueprint('user_bp', __name__)


