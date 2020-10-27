"""
    这是demo 02
"""
# @Time    : 2020/10/27 10:24
# @Author  : Libuda
# @FileName: demo_02_old.py
# @Software: PyCharm

#除非重新抛出异常，否则不建议使用`except Exception`捕获所有异常
# 应当使用finally子句来执行那些无论try块中有没有异常都应该被执行的代码
#`except`或`except Exception`会捕获语法错误、Ctrl+C中断等底层异常，而一般情况下这不是用户代码要处理的


try:
    file = open("1.txt")
except Exception as e:
    print(e)

