from flask import request, jsonify
from app.models.models import News

def news_show():
    nid = request.args.get('nid')
    news_item = News.query.filter_by(nid=nid).first()  

    if news_item:
        return jsonify({
            "title": news_item.title,
            "content": news_item.content,
            "img_url": news_item.img_url,
            "ymd": news_item.ymd.strftime('%Y-%m-%d %H:%M:%S') if news_item.ymd else None,
            "category": news_item.category,
            "j_info": news_item.j_info,
            "company": news_item.company,
            "cid" : news_item.cid
        })
    else:
        return jsonify({"error": "News item not found"}), 404