from stock import Stock
from history import History
from models import AddProductDTO

history = History()
stock = Stock(history)

print(stock.get_products())

product = AddProductDTO("Tesoura sem ponta", 5, "Rodrigo de Souza Fernandes")

print(stock.add_product(product))

print("____________Products____________")
print(stock.get_products())
print("____________History____________")
print(history.get_history(5))
print(stock.get_history())
