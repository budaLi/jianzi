# @Time    : 2020/6/24 20:39
# @Author  : Libuda
# @FileName: tutle数字.py
# @Software: PyCharm
# import turtle as t
# t.hideturtle()
# t.setup()
# t.penup()
# t.pencolor('red')
# t.write('2',font=("Times", 33, "normal"))
# t.fd(40)
# t.pencolor('blue')
# t.write('6',font=("Times", 33, "normal"))
# t.fd(40)
# t.pencolor('yellow')
# t.write('0',font=("Times", 33, "normal"))
# t.done()

def main(m):
    lis = [0,1,1]
    tem = 0
    while tem<=m:
        tem = lis[-2]+lis[-1]
        if tem>m:
            continue
        else:
            lis.append(tem)
    return lis

res = main(100)
print(res)
