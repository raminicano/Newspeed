from app import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    passwd = db.Column(db.String(255), nullable=False)
    id = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, nullable=False, default=db.func.current_timestamp())

class Log(db.Model):
    lid = db.Column(db.Integer, primary_key=True)
    action_time = db.Column(db.TIMESTAMP, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    action = db.Column(db.String(511))
    cid = db.Column(db.Integer, db.ForeignKey('cluster.cid'))

class News(db.Model):
    nid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(255))
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    ymd = db.Column(db.DateTime)
    com_num = db.Column(db.Integer, default=0)
    j_info = db.Column(db.String(255))
    company = db.Column(db.String(255))
    url = db.Column(db.Text)
    img_url = db.Column(db.Text)

class Cluster(db.Model):
    cid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    category = db.Column(db.String(255))
    clu_url = db.Column(db.Text)
    num = db.Column(db.Integer)

class Summary(db.Model):
    cid = db.Column(db.Integer, db.ForeignKey('cluster.cid'), primary_key=True)
    category = db.Column(db.String(255))
    keyword = db.Column(db.String(255))
    s_state = db.Column(db.String(255))
    sum_com = db.Column(db.Integer)

class Pdvl(db.Model):
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), primary_key=True)
    fv = db.Column(db.Float)

class NewsLog(db.Model):
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), primary_key=True)
    cid = db.Column(db.Integer, db.ForeignKey('cluster.cid'), primary_key=True)
    time = db.Column(db.Integer)


class UserCategories(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    politics = db.Column(db.Integer)
    economy = db.Column(db.Integer)
    society = db.Column(db.Integer)
    culture = db.Column(db.Integer)
    science = db.Column(db.Integer)
    world = db.Column(db.Integer)

class Bookmark(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    nid = db.Column(db.Integer, primary_key=True)
