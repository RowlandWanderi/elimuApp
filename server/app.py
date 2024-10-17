from models import db, User,Course,Enrollment
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS



from views import *
import random
import string

def generate_secret_key(length=32):
    characters = string.ascii_letters + string.digits
    secret_key = ''.join(random.choice(characters) for i in range(length))
    return secret_key

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
CORS(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(user_bp)
app.register_blueprint(course_bp)
app.register_blueprint(enrollment_bp)
app.register_blueprint(auth_bp)

jwt = JWTManager()
app.config["JWT_SECRET_KEY"] =  generate_secret_key()
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=24)
jwt.init_app(app)

@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header, jwt_data):
    jti = jwt_data['jti']
    token = TokenBlocklist.query.filter_by(jti=jti).first()
    if token:
        return token 
    else:
        return None



if __name__ == '__main__':
    app.run(port=5000, debug=True)