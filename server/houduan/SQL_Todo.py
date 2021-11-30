from operator import or_

from sqlalchemy.orm import exc
from ideas.database.Databases import Databases
from ideas.database.PMPapers import PMPapers
from ideas.database.graph import Graph
from ideas.database.WebLink import WebLink
from sqlalchemy import or_
import datetime
from ideas import db
import time
from CatchMed import CatchMed

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


# 数据库查找函数
def search_weblink(keys):
    res = []
    try:
        tars = WebLink.query.filter(or_(WebLink.title.like('%{}%'.format(keys)), WebLink.introduction.like('%{}%'.format(keys))) ).all()
        for tar in tars:
            dicts = {'Link_ID': tar.id, 'Title': tar.title,  'Url': tar.durl, 'Introduction': tar.introduction, "Date": tar.update_time}
            res.append(dicts)
    except Exception as e:
        print(e.__context__)
    return res


# 论文论文库添加函数
def papers(res):
    try:
        li = []
        for r in res:
            li.append(r['DBName'])
    except:
        return 601
    try:
        for l in li:
            spider = CatchMed(l)
            spider.get_URL()
            res = spider.rep()
            for r in res:
                try:
                    date = datetime.datetime.now()
                    r.append(date)
                    newp = PMPapers(r)
                    db.session.add(newp)
                    db.session.commit()
                except:
                    db.session.rollback()
            time.sleep(1)
    except:
        return 602
    return 200


# 论文库查找函数
def paper_search(mode, keys):
    res = []
    if mode == 'db':
        try:
            tars = PMPapers.query.filter(PMPapers.dbname == keys).all()
            for tar in tars:
                dicts = {'PM_ID': tar.pm_id, 'DBName': tar.dbname,  'Title': tar.paper_title, 'Authors': tar.authors_list, 'DOI': tar.DOI_text, 'Abstract': tar.Abstract, 'Url': tar.url_content, 'date': tar.date_time}
                res.append(dicts)
        except:
            pass
    elif mode == 'search':
        try:
            tars = PMPapers.query.filter(or_(PMPapers.paper_title.like('%{}%'.format(keys)), PMPapers.Abstract.like('%{}%'.format(keys))) ).all() 
            for tar in tars:
                dicts = {'PM_ID': tar.pm_id, 'DBName': tar.dbname,  'Title': tar.paper_title, 'Authors': tar.authors_list, 'DOI': tar.DOI_text, 'Abstract': tar.Abstract, 'Url': tar.url_content, 'date': tar.date_time}
                res.append(dicts)
        except:
            pass
    return res


# 更正DOI格式
def change_doi():
    res = []
    dbname = ''
    try:
        tars = PMPapers.query.filter(PMPapers.dbname.like('%{}%'.format(dbname))).all()
        for tar in tars:
            ss = str(tar.DOI_text)
            tar.DOI_text = ss.replace(' ', '')
            res.append({'dbname': tar.dbname, 'doi': tar.DOI_text})
        db.session.commit()
    except:
        pass
    return res


# 获取所有实体列表
def get_all_entities():
    result = Graph.query.with_entities(Graph.x, Graph.property, Graph.y).distinct().all()
    res = []
    for r in result:
        r = list(r)
        res.append(r)
    return res


# 更正摘要格式
def change_intro():
    res = []
    dbname = ''
    try:
        tars = Databases.query.filter(Databases.dbname.like('%{}%'.format(dbname))).all()
        for tar in tars:
            ss = tar.introduction
            if ss[0] == ':':
                ss = ss[1:]
            tar.introduction = ss
            res.append({'dbname': tar.dbname, 'introduction': tar.introduction})
        db.session.commit()
    except:
        pass
    return res
