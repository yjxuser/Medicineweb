from ideas import db


class Databases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dbname = db.Column(db.Text, unique=True)
    db_url = db.Column(db.Text, unique=True)
    introduction = db.Column(db.Text, unique=True)
    category = db.Column(db.Text, unique=True)
    date_time = db.Column(db.DateTime, unique=True)

    def __init__(self, dbname, db_url, introduction, category, date_time):
        self.dbname = dbname
        self.db_url = db_url
        self.introduction = introduction
        self.category = category
        self.date_time = date_time

    def __repr__(self):
        return '<Database %r>' % self.dbname

