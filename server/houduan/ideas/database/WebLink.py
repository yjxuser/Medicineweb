from ideas import db


class WebLink(db.Model):
    __tablename__ = "weblink"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    durl = db.Column(db.Text)
    introduction = db.Column(db.Text, unique=True)
    update_time = db.Column(db.DateTime)

    def __init__(self, iid, title, durl, introduction, date):
        self.iid = iid
        self.title = title
        self.durl = durl
        self.introduction = introduction
        self.update_time = date


    def __repr__(self):
        return '<WebLink %r>' % self.durl


