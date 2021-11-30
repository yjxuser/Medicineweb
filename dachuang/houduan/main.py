# import SqlActions
import json

import pymysql
from flask import request, jsonify
import SQL_Todo
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
