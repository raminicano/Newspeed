from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify
from app.models.models import Bookmark, News

@jwt_required()
def show_bookmark():
    uid = get_jwt_identity()

    # Bookmark 테이블에서 사용자의 북마크 가져오기
    bookmarks = Bookmark.query.filter_by(uid=uid).all()

    # Bookmark에서 nid 값들 추출
    nids = [bookmark.nid for bookmark in bookmarks]

    # News 테이블에서 해당 nid를 가진 뉴스 아이템 조회
    news_items = News.query.filter(News.nid.in_(nids)).all()

    # 뉴스 데이터 구성
    news_data = [{
        "title": item.title,
        "content": item.content,
        "nid": item.nid
    } for item in news_items]

    return jsonify(news_data)