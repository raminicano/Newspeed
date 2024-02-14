from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from app.auth import auth as auth_blueprint
from app.main import main as main_blueprint
from app.models import db  # db 인스턴스 임포트
from konlpy.tag import Mecab
from gensim.models.doc2vec import Doc2Vec

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Mecab 및 Doc2Vec 모델 초기화
    app.mecab = Mecab("/opt/homebrew/lib/mecab/dic/mecab-ko-dic")
    app.loaded_model = Doc2Vec.load("doc2vec_model")
    

    db.init_app(app)  # db 인스턴스를 애플리케이션과 함께 초기화

    return app


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(main_blueprint, url_prefix='/news')
