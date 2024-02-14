import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Doc2Vec
from sqlalchemy import text


def recommendation_for_user(user_id, model, session, mecab):

    recent_articles_query = text('''
        WITH ranked_news AS (
            SELECT
                n.content,
                n.title,
                n.cid,
                n.com_num,
                ROW_NUMBER() OVER (PARTITION BY n.cid ORDER BY n.com_num DESC) AS row_num
            FROM
                pn.news n
            LEFT JOIN
                pn.news_log nl ON n.cid = nl.cid
            WHERE
                nl.cid IS NULL
        )
        SELECT
            cid,
            title,
            content
        FROM
            ranked_news
        WHERE
            row_num = 1
        ORDER BY
            com_num DESC
        LIMIT 450;''')
    recent_articles = session.execute(recent_articles_query).fetchall()

    if not recent_articles:
        print("No recent articles found.")
        return None

    # 사용자의 pdvl 테이블 feature vector 가져오기
    user_pdvl_query = text('SELECT fv FROM pdvl WHERE uid = :user_id')
    user_pdvl_result = session.execute(user_pdvl_query, {'user_id': user_id}).fetchall()



    if not user_pdvl_result:
        print(f"No feature vector found for user {user_id}.")
        return None

    # 사용자의 feature vector
    numbers = [float(num) for num in user_pdvl_result[0][0][1:-1].split(',')]
    user_feature_vector = np.array(numbers)

    # 각 기사의 특징 벡터 추출 및 유사도 계산
    similarity_scores = []
    for article in recent_articles:
         # 열 이름 대신 정수 인덱스를 사용하여 데이터에 접근
        cid = article[0]
        title = article[1]
        content = article[2]
        article_vector = model.infer_vector(mecab.morphs(title + ' ' + content))
        similarity_score = cosine_similarity(user_feature_vector.reshape(1, -1), article_vector.reshape(1, -1))[0][0]
        similarity_scores.append((cid, similarity_score))

    # 유사도에 따라 정렬하여 가장 유사한 10개의 기사 추출
    top_similar_articles = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[:10]

    return top_similar_articles
