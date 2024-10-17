from models import db, Enrollment, User, Course
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity

enrollment_bp = Blueprint('enrollment_bp', __name__)

# Enroll in a Course
@enrollment_bp.route('/enroll', methods=['POST'])
@jwt_required()
def enroll_in_course():
    user_id = get_jwt_identity()  # Get the current user's ID
    data = request.get_json()
    course_id = data.get('course_id')

    # Check if the course exists
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "Course not found."}), 404

    # Check if the user is already enrolled in the course
    existing_enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if existing_enrollment:
        return jsonify({"error": "You are already enrolled in this course."}), 409

    # Create a new enrollment
    new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
    db.session.add(new_enrollment)
    db.session.commit()
    return jsonify({"success": "Successfully enrolled in the course!"}), 201


# View Enrolled Courses
@enrollment_bp.route('/enrollments', methods=['GET'])
@jwt_required()
def get_enrolled_courses():
    user_id = get_jwt_identity()  # Get the current user's ID
    enrollments = Enrollment.query.filter_by(user_id=user_id).all()

    enrolled_courses = []
    for enrollment in enrollments:
        course = Course.query.get(enrollment.course_id)
        if course:
            enrolled_courses.append({
                'course_id': course.id,
                'title': course.title,
                'description': course.description,
                'status': course.status,
            })

    return jsonify(enrolled_courses), 200


# Unenroll from a Course
@enrollment_bp.route('/enrollments/<int:course_id>', methods=['DELETE'])
@jwt_required()
def unenroll_from_course(course_id):
    user_id = get_jwt_identity()  # Get the current user's ID
    enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()

    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        return jsonify({"success": "Successfully unenrolled from the course!"}), 200
    else:
        return jsonify({"error": "You are not enrolled in this course."}), 404