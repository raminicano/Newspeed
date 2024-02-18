from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from app.models.models import db, Bookmark


@jwt_required()
def add_bookmark():
    uid = get_jwt_identity()
    data = request.json
    nid = data.get('nid')

    new_bookmark = Bookmark(uid=uid, nid=nid)
    db.session.add(new_bookmark)
    db.session.commit()

    return jsonify({'message': 'Bookmark added successfully!'}), 200