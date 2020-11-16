"""
    这是import规范demo
"""

import json

import flask
import torch

import xxx  # yes

# import torch

xxx.yyy1()

# 第一种
import utils
utils.tools.tools_print()


# 第二
from utils import tools,tools2

# 第三
from utils import tools
from utils import tools2


FLASK_SERVER = flask.Flask(__name__)
FLASK_SERVER.route("/")


# TODO  xxx
def index():
    """
    这是一个接口
    :return:
    """
    res = {"msg": "这是一个接口"}
    print("123", "2444")
    value = torch.max([1, 2])
    print(value)
    return json.dumps(res)


def _new_index():
    res = {"msg": "这是一个接口"}
    return json.dumps(res)


if __name__ == "__main__":
    FLASK_SERVER.run(debug=False)
