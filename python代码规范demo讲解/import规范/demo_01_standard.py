"""
    这是import规范demo
"""
# @Time    : 2020/10/27 10:07
# @Author  : Libuda
# @FileName: demo_01.py
# @Software: PyCharm

import json

import flask

FLASK_SERVER = flask.Flask(__name__)
FLASK_SERVER.route("/")


def index():
    """
    这是一个接口
    :return:
    """
    res = {"msg": "这是一个接口"}
    return json.dumps(res)


if __name__ == "__main__":
    FLASK_SERVER.run(debug=False)
