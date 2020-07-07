
def q1():
    # 最终账户余额
    final_account_value = float(input("Enter the final account value:"))
    # 年利率
    interest_rate = float(input("Enter the annual interest rate:"))/100
    # 年
    year = int(input("Enter the number of year :"))

    initialDepositAmout = final_account_value/((1+interest_rate)**year)

    print("The initial value is :{}".format(initialDepositAmout))


q1()