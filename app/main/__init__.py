from flask import Blueprint
from .hot_topics import get_hot_topics
from .recommendations import get_recommendations

# main 블루프린트 생성
main = Blueprint('main', __name__)

main.add_url_rule('/hot-topics', view_func=get_hot_topics, methods=['GET'])
main.add_url_rule('/recommendations', view_func=get_recommendations, methods=['GET'])