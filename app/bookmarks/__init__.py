from flask import Blueprint
from .add import add_bookmark
from .inquiry import show_bookmark
from .remove import delete_bookmark

bookmarks = Blueprint('bookmarks', __name__)

bookmarks.add_url_rule('/add', view_func=add_bookmark, methods=['POST'])
bookmarks.add_url_rule('/inquiry', view_func=show_bookmark, methods=['GET'])
bookmarks.add_url_rule('/remove', view_func=delete_bookmark, methods=['DELETE'])

