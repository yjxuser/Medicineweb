# import SqlActions
import json

import pymysql
from flask import request, jsonify
import SQL_Todo
import Get_Info
from Neo4jWork import create_graph
from ideas import create_app

pymysql.install_as_MySQLdb()

app = create_app()


@app.route('/db/<mode>', methods=['GET', 'POST'])
def SQL_Works(mode):
    if mode == 'search':
        dbname = request.args.get('dbname')
        if dbname is None:
            dbname = ""
        instances = SQL_Todo.search(dbname)
        if not instances:
            res = {'status': 304, 'message': 'error', 'results': instances}
        else:
            res = {'status': 200, 'message': 'success', 'results': instances}
        return jsonify(res)
    elif mode == 'delete' and request.method == 'GET':
        dbname = request.args.get('dbname')
        if dbname is None:
            res = {'status': 404, 'message': 'None', 'results': []}
        status = SQL_Todo.del_by_title(dbname)
        if status == 200:
            res = {'status': 200, 'message': 'success'}
        else:
            res = {'status': 304, 'message': 'error'}
        return jsonify(res)
    elif mode == 'change':
        data = json.loads(request.data)
        dbname = data['dbname']
        db_url = data['db_url']
        introduction = data['introduction']
        category = data['category']
        instances = SQL_Todo.change(dbname, db_url, introduction, category)
        if not instances:
            res = {'status': 303, 'message': 'error', 'results': instances}
        else:
            res = {'status': 200, 'message': 'success', 'results': instances}
        return res
    elif mode == 'add' and request.method == 'POST':
        data = json.loads(request.data)
        dbname = data['dbname']
        db_url = data['db_url']
        introduction = data['introduction']
        category = data['category']
        instances = SQL_Todo.add(dbname, db_url, introduction, category)
        if not instances:
            res = {'status': 305, 'message': 'error', 'results': instances}
        else:
            res = {'status': 200, 'message': 'success', 'results': instances}
        return jsonify(res)


@app.route('/spider/get', methods=['GET', 'POST'])
def get_papers():
    if request.method == 'GET':
        dbname = request.args.get('dbname')
        if dbname is None:
            dbname = ""
        instances = SQL_Todo.search(dbname)
        status = SQL_Todo.papers(instances)
        res = {'status': status}
        return jsonify(res)


@app.route('/weblink', methods=['GET'])
def get_links():
    if request.method == 'GET':
        keywords = request.args.get('wd')
        print(keywords, type(keywords))
        if keywords == '':
            res = {'status': 404, 'message': 'error', 'results': []}
        else:
            instances = SQL_Todo.search_weblink(keywords)
            if not instances:
                res = {'status': 304, 'message': 'error', 'results': instances}
            else:
                res = {'status': 200, 'message': 'success', 'results': instances}
    return jsonify(res)


@app.route('/papers/<mode>', methods=['GET'])
def db_papers(mode):
    if mode == 'db':
        dbname = request.args.get('name')
        if dbname is None:
            dbname = ""
        instances = SQL_Todo.paper_search(mode, dbname)
        if not instances:
            res = {'status': 304, 'message': 'error', 'results': instances}
        else:
            res = {'status': 200, 'message': 'success', 'results': instances}
    elif mode == 'search':
        keywords = request.args.get('wd')
        print(keywords, type(keywords))
        if keywords == '':
            res = {'status': 404, 'message': 'error', 'results': []}
        else:
            instances = SQL_Todo.paper_search(mode, keys=keywords)
            if not instances:
                res = {'status': 304, 'message': 'error', 'results': instances}
            else:
                res = {'status': 200, 'message': 'success', 'results': instances}
    return jsonify(res)


@app.route('/upgrade', methods=['GET'])
def update():
    res = Get_Info.Gene_cards()
    ret = []
    for dic in res:
        r = SQL_Todo.add(dic['DBName'], dic['DBUrl'], dic['Introduction'], dic['category'])
        print(r)
    return jsonify(ret)


@app.route('/introduction', methods=['GET'])
def doi_up():
    res = SQL_Todo.change_intro()
    return jsonify(res)


@app.route('/entities', methods=['GET'])
def get_entities():
    triples = SQL_Todo.get_all_entities()
    res = create_graph(triples)

    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
