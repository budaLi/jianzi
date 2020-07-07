# @Time    : 2020/6/30 12:30
# @Author  : Libuda
# @FileName: main.py
# @Software: PyCharm

def main():
    N = input("请输入N(N为数字且大于0)")
    Res = input("请输入RES字符串")
    Var = input("请输入Var字符串")
    res_path = "res.txt"

    N = int(N)

    res_lis=[]
    for n in range(2,N+1):
        tem = "T{}:=({}*{}".format(n,n,Var)
        for i in range(-n+1,-1):
            i = -i
            tem+="+{}*{}({},{})".format(i,Res,Var,(n-i))
        tem+="+{}({},{}))/{};".format(Res,Var,n-1,sum([j for j in range(1,n+1)]))
        print(tem)
        res_lis.append(tem)
    with open(res_path,"w") as f:
        for one in res_lis:
            f.write(one+"\n")
main()