from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    id = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    # 예시: 카테고리 선택이 필수가 아니라면, 필드 및 검증 로직을 조정해야 합니다.
    politics = IntegerField('Politics')
    economy = IntegerField('Economy')
    society = IntegerField('Society')
    culture = IntegerField('Culture')
    science = IntegerField('Science')
    world = IntegerField('World')
    submit = SubmitField('Sign Up')

    def validate_id(self, id):
        user = User.query.filter_by(id=id.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
