from flask import render_template, redirect, url_for, flash, request, jsonify
from .forms import RegistrationForm
from app.models.models import db, User, UserCategories
from flask import current_app
from app import bcrypt


def register_user():
    form = RegistrationForm()
    if form.validate_on_submit():  # 폼 제출 시 데이터 유효성 검증
        hashed_password = current_app.bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        user = User(id=form.id.data, email=form.email.data, passwd=hashed_password)
        
        db.session.add(user)
        db.session.commit()

        # 카테고리 데이터 생성 및 저장
        new_user_categories = UserCategories(
            uid=user.uid, 
            politics=form.politics.data,
            economy=form.economy.data,
            society=form.society.data,
            culture=form.culture.data,
            science=form.science.data,
            world=form.world.data
        )
        db.session.add(new_user_categories)
        db.session.commit()

        return jsonify({'message': '회원가입 성공!'}), 201

    return jsonify({'message': '잘못된 요청입니다.'}), 400
