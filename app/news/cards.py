from flask import request, jsonify
from app.models.models import News, Summary

categories = ['politics', 'economy', 'society', 'culture', 'science', 'world']


def news_cards():
    news_data = []
    for category in categories:
        result1 = Summary.query.with_entities(Summary.category, Summary.cid).filter_by(category=category).order_by(Summary.sum_com.desc()).first()
        result2 = News.query.filter_by(cid=result1.cid).order_by(News.com_num.desc()).first()
        news_data.append({"title" : result2.title, "content": result2.content, "nid": result2.nid})
    
    
    return jsonify(news_data)