import datetime

class Stock:
    def __init__(self, symbol):
        self.symbol = symbol
        self.price = 0.0
        self.history = {}
    
    def __repr__(self):    
        return f"{self.symbol}"
    
    def setPrice(self, price, date):
        self.price = price
        self.history[date] = price
        # self.history[datetime.now()] = price