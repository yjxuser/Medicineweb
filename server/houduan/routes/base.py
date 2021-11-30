from flask import Flask, request, jsonify, Blueprint

sum = Blueprint('sum', __name__)

def get_sum(x, y):
    result = x + y
    return result



def get_result():
    x = request.args.get('first')
    y = request.args.get('second')
    res = get_sum(x, y)
    return str(res)

