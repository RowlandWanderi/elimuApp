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

# Create a course
@course_bp.route('/courses', methods=['POST'])
@jwt_required()
def create_course():
    user_id = get_jwt_identity()
    data = request.get_json()

    new_course = Course(
        title=data['title'],
        description=data['description'],
        status='Pending',  # All courses start with 'Pending' status
        instructor_id=user_id
    )
    db.session.add(new_course)
    db.session.commit()

    return jsonify({'success': 'Course created successfully'}), 201

# Update a course (Instructors only)
@course_bp.route('/courses/<int:id>', methods=['PUT'])
@jwt_required()
def update_course(id):
    user_id = get_jwt_identity()
    course = Course.query.get(id)

    if course is None:
        return jsonify({'error': 'Course not found'}), 404

    if course.instructor_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    data = request.get_json()
    course.title = data.get('title', course.title)
    course.description = data.get('description', course.description)
    
    # Instructor cannot change the status directly
    db.session.commit()

    return jsonify({'success': 'Course updated successfully'}), 200

# Delete a course (Instructors only)
@course_bp.route('/courses/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_course(id):
    user_id = get_jwt_identity()
    course = Course.query.get(id)

    if course is None:
        return jsonify({'error': 'Course not found'}), 404

    if course.instructor_id != user_id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(course)
    db.session.commit()

    return jsonify({'success': 'Course deleted successfully'}), 200

# Approve a course (Approvers only)
@course_bp.route('/courses/<int:id>/approve', methods=['POST'])
@jwt_required()
def approve_course(id):
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user.role != 'Approver':
        return jsonify({'error': 'Unauthorized'}), 403

    course = Course.query.get(id)

    if course is None:
        return jsonify({'error': 'Course not found'}), 404

    course.status = 'Approved'
    db.session.commit()

    return jsonify({'success': 'Course approved successfully'}), 200