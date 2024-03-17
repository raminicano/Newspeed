from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from konlpy.tag import Mecab
from gensim.models.doc2vec import Doc2Vec
from config import Config
from flask_jwt_extended import JWTManager  


db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    #bcrypt = Bcrypt(app)
    bcrypt.init_app(app)
    jwt = JWTManager(app)

    # Mecab 및 Doc2Vec 모델 초기화 및 앱 객체에 추가
    mecab_path = app.config.get('MECAB_PATH')  # 예시 경로
    doc2vec_model_path = app.config.get('DOC2VEC_MODEL_PATH')

    app.mecab = Mecab(mecab_path)
    app.loaded_model = Doc2Vec.load(doc2vec_model_path)
    with app.app_context():
        from app.auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint, url_prefix='/auth')

        from app.news import news as news_blueprint
        app.register_blueprint(news_blueprint, url_prefix='/news')

        from app.bookmarks import bookmarks as bookmarks_blueprint
        app.register_blueprint(bookmarks_blueprint, url_prefix='/bookmarks')

    return app