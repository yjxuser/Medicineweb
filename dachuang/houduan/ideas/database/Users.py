from ideas import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    date = db.Column(db.DateTime, unique=True)

    def __init__(self, username, password, date):
        self.username = username
        self.password = password
        self.date = date

    def __repr__(self):
        return '<User %r>' % self.username
# 引入配置文件必须在创建数据库连接之前
