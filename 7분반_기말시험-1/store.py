class Store :
    def __init__(self, menu_price):
        self.price = menu_price
        self.revenue = 0

    def sell(self, menu, n_sell):
        self.revenue += self.price[menu]*n_sell