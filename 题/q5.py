
def q5():

    # 判断是否是质数
    def judge(m):
        # 2为质数
        if m==2: return True
        for i in range(2,int(m/2)+1):
            if m%i==0:
                return False
        return True


    number = input("Please input a number:")
    try:
        number = int(number)
        res = []
        for i in range(2, number):
            if judge(i):
                res.append(i)

        for i in range(0, len(res)):
            if i % 8 == 0:
                print("\n")
            print(str(res[i]), end="\t")

    except Exception:
        print("Please input integer number,you input is {}".format(type(number)))


q5()