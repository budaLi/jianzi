
def q3():
    number = int(input("Please input a number:"))

    #必须保证number>0
    if number<0:
        print("Please input a number>0")

    res = 1
    while res**2<number:
        res+=1
    print(res)


q3()
