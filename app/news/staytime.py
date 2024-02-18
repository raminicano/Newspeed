from flask import request, jsonify
from flask_jwt_extended import decode_token
from app.models.models import db, NewsLog

def news_stayTime():
    data = request.json
    decoded_token = decode_token(data.get('token'))
    uid = decoded_token['sub']
    new_time = data.get('time')
    cid = data.get('cid')
    check = NewsLog.query.filter_by(uid=uid, cid=cid).first()
    if check:
        check.time += new_time
        db.session.commit()
        return jsonify({'message': 'log updated successfully!'}), 200
    else:
        new_log = NewsLog(uid=uid, cid=cid, time=new_time)
        db.session.add(new_log)
        db.session.commit()
        return jsonify({'message': 'log added successfully!'}), 200
