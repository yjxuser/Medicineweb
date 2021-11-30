from ideas.database.Databases import Databases
import datetime
from ideas import db


# 数据库增加数据函数
def add(dbname, db_url, introduction, category):
    res = []
    try:
        date = datetime.datetime.now()
        newp = Databases(dbname, db_url, introduction, category, date)
        db.session.add(newp)
        db.session.commit()
    except:
        pass
    tar = Databases.query.filter(Databases.dbname == dbname).first()
    dicts = {'ID': tar.id, 'DBName': tar.dbname,  'DBUrl': tar.db_url, 'Introduction': tar.introduction, 'date': tar.date_time}
    res.append(dicts)
    return res


# 数据库删除数据函数
def del_by_title(dbname):
    try:
        res = Databases.query.filter_by(dbname=dbname).first()
        db.session.delete(res)
        db.session.commit()
    except:
        return 404
    return 200


def del_by_id(iid):
    res = Databases.query.filter_by(id=iid).first()
    db.session.delete(res)
    db.session.commit()


# 数据库修改数据函数
def change(dbname, db_url, introduction, category):
    res = []
    try:
        date = datetime.datetime.now()
        change_target = Databases.query.filter(Databases.dbname == dbname).first()
        change_target.db_url = db_url
        change_target.introduction = introduction
        change_target.category = category
        change_target.date = date
        db.session.commit()
        tar = Databases.query.filter(Databases.dbname == dbname).first()
        dicts = {'ID': tar.id, 'DBName': tar.dbname,  'DBUrl': tar.db_url, 'Introduction': tar.introduction, 'date': tar.date_time}
        res.append(dicts)
    except:
        pass
    return res


# 数据库查找函数
def search(dbname):
    res = []
    try:
        tars = Databases.query.filter(Databases.dbname.like('%{}%'.format(dbname))).all()
        for tar in tars:
            dicts = {'ID': tar.id, 'DBName': tar.dbname,  'DBUrl': tar.db_url, 'Introduction': tar.introduction, 'date': tar.date_time}
            res.append(dicts)
    except:
        pass
    return res
