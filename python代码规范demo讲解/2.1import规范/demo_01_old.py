# @Time    : 2020/10/27 10:07
# @Author  : Libuda
# @FileName: demo_01.py
# @Software: PyCharm

# 必须按标准库、第三方库、应用程序自有库的顺序排列import，每部分之间留一个空行。
# 每行只能导入一个库
from flask import Flask
from json import dumps, dump

# 模块级常量应当全大写，以下划线连接，比如PI，HOUSE_VALUE。
flask_server = Flask(__name__)
flask_server.route("/")

# 函数应有功能注释

def Index():
    res = {"msg": "这是一个接口"}
    print("123", "2444")
    return dumps(res)

if __name__ == "__main__":
    flask_server.run(debug=False)

