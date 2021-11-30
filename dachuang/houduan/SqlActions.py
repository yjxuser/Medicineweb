from ideas.database.Users import Users
import datetime
from ideas import db


# 数据库增加数据函数
def add(username, password):
    res = []
    try:
        date = datetime.datetime.now()
        newp = Users(username, password, date)
        db.session.add(newp)
        db.session.commit()
    except:
        pass
    tar = Users.query.filter(username == username).first()
    dicts = {'ID': tar.user_id, 'Username': tar.username,  'password': tar.password, 'date': tar.date}
    res.append(dicts)
    return res


# 数据库删除数据函数
def del_by_title(username):
    try:
        res = Users.query.filter_by(username=username).first()
        db.session.delete(res)
        db.session.commit()
    except:
        return 404
    return 200


def del_by_id(iid):
    res = Users.query.filter_by(user_id=iid).first()
    db.session.delete(res)
    db.session.commit()


# 数据库修改数据函数
def change(pre_pwd, uname, new_pwd):
    res = []
    try:
        date = datetime.datetime.now()
        change_target = Users.query.filter(Users.username == uname).first()
        change_target.password = new_pwd
        change_target.date = date
        db.session.commit()
        tar = Users.query.filter(Users.username == uname).first()
        dicts = {'ID': tar.user_id, 'Username': tar.username,  'password': tar.password, 'date': tar.date}
        res.append(dicts)
    except:
        pass
    return res


# 数据库查找函数
def search(username):
    res = []
    try:
        tars = Users.query.filter(Users.username.like('%{}%'.format(username))).all()
        for tar in tars:
            dicts = {'ID': tar.user_id, 'Username': tar.username,  'password': tar.password, 'date': tar.date}
            res.append(dicts)
    except:
        pass
    return res
