from models import Product, StockMovement, AddProductDTO
from datetime import datetime

class Stock:
    def __init__(self):
        self.__products: list[Product] = []
        self.__history: list[StockMovement]

    def get_product_by_name(self, name:str) -> Product | None:
        return next((p for p in self.__products if p.name == name), None)
    
    def get_product_by_id(self, id:int) -> Product | None:
        return next((p for p in self.__products if p.id == id), None)

    def add_product(self, product:AddProductDTO) -> None:
        stock_product: Product = self.get_product_by_name(product.name)

        if stock_product:

            movement = StockMovement()
            movement.operator = product.operator
            movement.product = stock_product
            movement.date = datetime.now()

            stock_product.quantity += product.quantity
            # call update product function

            # call add stock movement on history function
        
        else:
            next_id: int = self.__products[-1].id + 1 if len(self.__products) > 0 else 1
            new_product: Product = Product()
            new_product.id = next_id
            new_product.name = product.name
            new_product.quantity = product.quantity

            self.__products.append(new_product)



