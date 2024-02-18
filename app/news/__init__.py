from flask import Blueprint
from .hot_topics import get_hot_topics
from .recommendations import get_recommendations
from .summary import get_news_by_id
from .show import news_show
from .cards import news_cards
from .staytime import news_stayTime

news = Blueprint('news', __name__)

news.add_url_rule('/hot-topics', view_func=get_hot_topics, methods=['GET'])
news.add_url_rule('/recommendations', view_func=get_recommendations, methods=['GET'])
news.add_url_rule('/summary', view_func=get_news_by_id, methods=['GET'])
news.add_url_rule('/show', view_func=news_show, methods=['GET'])
news.add_url_rule('/cards', view_func=news_cards, methods=['GET'])
news.add_url_rule('/staytime', view_func=news_stayTime, methods=['POST'])