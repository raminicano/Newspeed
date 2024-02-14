from flask import Blueprint
from .login import login_user
from .register import register_user

# Auth 블루프린트 생성
auth = Blueprint('auth', __name__)

auth.add_url_rule('/login', view_func=login_user, methods=['POST'])
auth.add_url_rule('/register', view_func=register_user, methods=['POST'])

