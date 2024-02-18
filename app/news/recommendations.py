from flask import jsonify, request
from flask import current_app

from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.models import db, NewsLog, UserCategories, Summary
from app.recommend.pdvl_updater import PDVLUpdater
from app.recommend.recommendation_module import recommendation_for_user
from .normalize import normalize_integer_sum

categories = ['politics', 'economy', 'society', 'culture', 'science', 'world']


@jwt_required()
def get_recommendations():
    uid = get_jwt_identity()
    # 애플리케이션 컨텍스트에서 Mecab 및 Doc2Vec 모델 인스턴스에 접근
    mecab = current_app.mecab
    loaded_model = current_app.loaded_model
    check = NewsLog.query.filter_by(uid=uid).all()
    # 전송할 데이터
    news_data = []
    # 로그 데이터를 사용하는 경우
    if len(check) >= 3:
        # 3의 배수마다 업데이트
        if len(check) % 3 == 0:
            updater = PDVLUpdater(loaded_model, db.session)
            updater.update_pdvl_table(uid)
            # print('업데이트 완료')
        
        recommended_articles = recommendation_for_user(uid, loaded_model, db.session, mecab)
        for cid, score in recommended_articles:
            score = int(score * 1000)
            news_items = db.session.query(
                Summary.keyword,
                Summary.cid
            ).filter(Summary.cid==cid).first()

            news_data.append({
                    "keyword": news_items.keyword,
                    "sum_com": score,
                    "cid": news_items.cid
                })
    # 초기 값을 사용하는 경우
    else:
        results = db.session.query(
            UserCategories.politics,
            UserCategories.economy,
            UserCategories.society,
            UserCategories.culture,
            UserCategories.science,
            UserCategories.world,
        ).filter(UserCategories.uid == uid).first()

        # 결과를 리스트로 변환하고 정규화
        scores = normalize_integer_sum(list(results), 10)
        
        # 각 카테고리별로 뉴스 조회
        for category, score in zip(categories, scores):
            news_items = db.session.query(
                Summary.keyword,
                Summary.sum_com,
                Summary.cid
            )\
            .filter(Summary.category == category)\
            .order_by(Summary.sum_com.desc())\
            .limit(score)\
            .all()
            for item in news_items:
                news_data.append({
                    "keyword": item.keyword,
                    "sum_com": item.sum_com,
                    "cid": item.cid
                })
   
    return jsonify(news_data)

