# Q8

class Bread :
    price = 1000
    ## your code here!
    def __init__(self):
        self.price = Bread.price
    def changePrice(self,price):
        self.price = price
    ##


# print output
bread = Bread()
print(bread.price)

bread.changePrice(1200)
print(bread.price)
