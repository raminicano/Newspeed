from flask import render_template, redirect, url_for, flash, request, jsonify
from .forms import RegistrationForm
from app.models.models import db, User, UserCategories
from flask import current_app
from app import bcrypt


# def register_user():
#     form = RegistrationForm()
#     if form.validate_on_submit():  # 폼 제출 시 데이터 유효성 검증
#         #hashed_password = current_app.bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

#         user = User(id=form.id.data, email=form.email.data, passwd=hashed_password)
        
#         db.session.add(user)
#         db.session.commit()


#         new_user = User(id=form.id.data, email=form.email.data, passwd=hashed_password)
#         categories_data = request.json['category']
#         # 유저 카테고리 데이터를 user_categories 테이블에 저장
#         new_user_categories = UserCategories(uid=new_user.uid, politics=categories_data[0],
#                                             economy=categories_data[1], society=categories_data[2],
#                                             culture=categories_data[3], science=categories_data[4],
#                                             world=categories_data[5])
#         db.session.add(new_user_categories)
#         db.session.commit()
    
    
#         return jsonify({'message': '회원가입 성공!'}), 201

#     else:     
#         return jsonify({'message': '잘못된 요청입니다.'}), 400




def register_user():
    data = request.json
    email = data['email']
    user_id = data['id']
    password = data['passwd']
    categories_data = data['category']

    try:
        existing_user = User.query.filter((User.id == user_id) | (User.email == email)).first()
        if existing_user:
            return jsonify({'message': '이미 존재하는 사용자 이름이나 이메일입니다.'}), 400
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(id=user_id, email=email, passwd=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # 유저 카테고리 데이터를 user_categories 테이블에 저장
        new_user_categories = UserCategories(
            uid=new_user.uid, 
            politics=categories_data[0],
            economy=categories_data[1], 
            society=categories_data[2],
            culture=categories_data[3], 
            science=categories_data[4],
            world=categories_data[5]
        )
        db.session.add(new_user_categories)
        db.session.commit()

    except Exception as e:
        db.session.rollback()  # 롤백을 통해 데이터베이스의 일관성 유지
        return jsonify({'message': '회원가입 처리 중 오류가 발생했습니다.', 'error': str(e)}), 500

    return jsonify({'message': '회원가입 성공!'}), 201

