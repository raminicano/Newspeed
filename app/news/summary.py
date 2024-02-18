from flask import request, jsonify
from app.models.models import Summary, News


def get_news_by_id():
    cid = request.args.get('cid')
    summary = Summary.query.filter_by(cid=cid).first()

    if summary:
        news_items = News.query.filter_by(cid=cid).order_by(News.com_num.desc()).limit(10).all()
        news_data = [{
            "title": item.title,
            "content": item.content,
            "nid": item.nid
        } for item in news_items]

        result = {
            "keyword" : summary.keyword,
            "s_state": summary.s_state,
            "articles": news_data
        }

        return jsonify(result)
    else:
        return jsonify({"message": "No summary found for the provided news ID"}), 404