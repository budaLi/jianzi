
from math import sin
from math import cos
from math import tan

def q6():
    data = input("Please input function(sin cos tan),a,b and n using space split it:")
    data = data.split()

    #eval can alternative sin cos or tan
    f  = eval(data[0])
    a = int(data[1])
    b = int(data[2])

    n = eval(data[3])
    if  isinstance(n,int):

        res = 0
        for i in range(1,n):
            res += (b-a)/n*f(a+(b-a)/n*(i-1/2))

        print(res)
    else:
        print("n required int ,but is {}".format(type(n)))


q6()
