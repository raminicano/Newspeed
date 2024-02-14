from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from app.models.models import db, User
from app import bcrypt

# auth 블루프린트 인스턴스를 생성합니다. 이 코드는 __init__.py 파일에 있어야 함
# auth = Blueprint('auth', __name__)


def login_user():
    data = request.json
    user_id = data['id']
    password = data['passwd']
    user = User.query.filter_by(id=user_id).first()
    if user and bcrypt.check_password_hash(user.passwd, password):
        token = create_access_token(identity=user.uid)
        return jsonify({"token": token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
