import json
from tqdm import tqdm
from sqlalchemy import text


class PDVLUpdater:
    def __init__(self, model, session):
        self.model = model
        self.session = session

    def update_pdvl_table(self, user_id):
        select_query = text('SELECT cid, time FROM pn.news_log where uid = :user_id;')
        result = self.session.execute(select_query, {'user_id':user_id}).fetchall()

        aggregated_feature_vectors = {}
        for row in tqdm(result, total=len(result)):
            news_id, total_time = row[0], float(row[1])
            weighted_vector = total_time * self.model.dv[news_id]

            if user_id in aggregated_feature_vectors:
                aggregated_feature_vectors[user_id] += weighted_vector
            else:
                aggregated_feature_vectors[user_id] = weighted_vector


        for uid, feature_vector in aggregated_feature_vectors.items():
            feature_vector_str = json.dumps(feature_vector.tolist())
            update_query = text('''
                INSERT INTO pn.pdvl (uid, fv)
                VALUES (:uid, :fv)
                ON DUPLICATE KEY UPDATE fv = :fv;
            ''')

            self.session.execute(update_query, {'uid': uid, 'fv': feature_vector_str})

        try:
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e
