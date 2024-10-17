from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime

db = SQLAlchemy()

    
class User(db.Model):
    __tablename__ = 'user'
    
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    role = db.Column(db.String(80), nullable=False)
    
    #relationships
    courses = db.relationship('Course', back_populates='user', lazy=True, cascade='all, delete-orphan')
    enrollments = db.relationship('Enrollment', back_populates='student', lazy=True, cascade='all, delete-orphan')  # For student enrollments
   
   #validate the users email to have an @
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("Invalid email address. Must contain '@'.")
        return email
    
#   For Logout JWT Block List
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti =  db.Column(db.String(100),nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    

class Course(db.Model ):
    __tablename__ = 'courses'
    
    
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    status = db.Column(db.String(20), default='Pending')  # New column for course status
    #foreign key to user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    #relationship
    user = db.relationship('User', back_populates='courses', cascade="all, delete")
    enrollments = db.relationship('Enrollment', back_populates='course', lazy=True, cascade='all, delete-orphan')  # Students' enrollment to this course
    
class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # Foreign keys
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    
    # Relationships
    student = db.relationship('User', back_populates='enrollments')  # The student who enrolls
    course = db.relationship('Course', back_populates='enrollments')  # The course being enrolled in