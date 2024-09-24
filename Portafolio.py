import Stock
import datetime
import math

class Portafolio:
    def __init__(self):
        self.inversiones = {}

    def addInvestment(self, stock, quantity):
        self.inversiones[stock] = quantity

    def increaseInvestment(self, stock, quantity):
        self.inversiones[stock] += quantity

    def profit(self, startdate, enddate):
        start_value = sum(stock.history[startdate] * quantity for stock, quantity in self.inversiones.items())
        end_value = sum(stock.history[enddate] * quantity for stock, quantity in self.inversiones.items())
        return end_value - start_value
    
    def annualizedReturn(self, startdate, enddate): #retorna porcentualmente el retorno anualizado
        start_value = sum(stock.history[startdate] * quantity for stock, quantity in self.inversiones.items())
        end_value = sum(stock.history[enddate] * quantity for stock, quantity in self.inversiones.items())
        
        total_return = (end_value - start_value) / start_value
        days = (enddate - startdate).days
        
        return (math.pow(1 + total_return, 365 / days) - 1)*100


folio = Portafolio()
stock = Stock.Stock("AAPL")

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=180)


stock.setPrice(100, yesterday)
stock.setPrice(120, today)

folio.addInvestment(stock, 1)

print(folio.profit(yesterday, today))
print(folio.annualizedReturn(yesterday, today)) 