from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from app.models.models import User

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    id = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    # confirm_password 필드 제거
    # 카테고리 별 필드 제거 및 category 배열 처리 방법 고려 필요
    submit = SubmitField('Sign Up')

    def validate_id(self, id):
        user = User.query.filter_by(id=id.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


    # politics = IntegerField('Politics')
    # economy = IntegerField('Economy')
    # society = IntegerField('Society')
    # culture = IntegerField('Culture')
    # science = IntegerField('Science')
    # world = IntegerField('World')