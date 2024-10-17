from models import db, User, TokenBlocklist
from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, get_jwt



auth_bp = Blueprint('auth_bp', __name__)


