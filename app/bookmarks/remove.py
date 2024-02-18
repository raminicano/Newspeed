from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from app.models.models import db, Bookmark

@jwt_required()
def delete_bookmark():
    uid = get_jwt_identity()
    data = request.json
    nid = data.get('nid')

    bookmark_to_delete = Bookmark.query.filter_by(uid=uid, nid=nid).first()

    if bookmark_to_delete:
        db.session.delete(bookmark_to_delete)
        db.session.commit()
        return jsonify({'message': 'Bookmark deleted successfully!'}), 200
    else:
        return jsonify({'message': 'Bookmark not found'}), 404
