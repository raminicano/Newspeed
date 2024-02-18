from flask import jsonify, request
from app.models.models import db, Summary


def get_hot_topics():
    category = request.args.get('category')

    results = db.session.query(
        Summary.keyword,
        Summary.sum_com,
        Summary.cid
    ).filter(Summary.category == category)\
     .order_by(Summary.sum_com.desc())\
     .limit(10)\
     .all()

    news_data = [{"keyword": result.keyword, "sum_com": result.sum_com, "cid": result.cid} for result in results]
    return jsonify(news_data)
