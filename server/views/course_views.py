from models import db,User
from flask import Blueprint, jsonify, request,make_response
from flask_jwt_extended import  jwt_required, get_jwt_identity


course_bp = Blueprint('course_bp', __name__)

