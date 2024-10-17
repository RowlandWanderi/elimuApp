from models import db,User,Course
from flask import Blueprint, jsonify, request,make_response
from flask_jwt_extended import  jwt_required, get_jwt_identity


course_bp = Blueprint('course_bp', __name__)

# Fetch all courses
@course_bp.route('/courses', methods=['GET'])
def get_all_courses():
    courses_list = []
    courses = Course.query.all()

    for course in courses:
        course_data = {
            'id': course.id,
            'title':course.title,
            'description': course.description,
            'status' : course.status,
            
        }
        courses_list.append(course_data)
    return jsonify(courses_list), 200


#fetch a single course
@course_bp.route('/courses/<int:id>', methods=['GET'])
def get_course_by_id(id):
    course = Course.query.get(id)
    
    if course is None:
        return jsonify({'error': 'course not found'}), 404

    course_data = {
        'id': course.id,
        'title':course.title,
        'description': course.description,
    }
    return jsonify(course_data), 200