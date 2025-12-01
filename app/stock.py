from models import Product, StockMovement, AddProductDTO, WithdrawProductDTO
from datetime import datetime
from history import History

class Stock:
    def __init__(self, history: History):
        self.__products: list[Product] = [
            Product(1, "Papel A4", 50),
            Product(2, "Caneta esferográfica", 120),
            Product(3, "Lápis", 80),
            Product(4, "Borracha", 40),
            Product(5, "Grampeador", 10),
            Product(6, "Caixas de papelão", 25),
            Product(7, "Fita adesiva", 30),
            Product(8, "Luvas de proteção", 100),
            Product(9, "Máscara descartável", 200),
            Product(10, "Detergente", 15)
        ]

        self.__history = history

    def get_history(self):
        return self.__history.get_history(5)
    
    def get_products(self) -> list[Product]:
        return self.__products

    def get_products_by_name(self, name:str) -> list[Product] | list:
        return [p for p in self.__products if name.lower() in p.name.lower()]
    
    def get_product_by_id(self, id:int) -> Product | None:
        return next((p for p in self.__products if p.id == id), None)
    
    def update_product(self, product: Product) -> None:
        index = next((i for i, item in enumerate(self.__products) if item.id == product.id), None)
        if (index is None): raise Exception("Id não encontrado na lista de produtos")
        self.__products[index].quantity = product.quantity

    def add_product(self, product:AddProductDTO) -> None:
        stock_product: Product = self.get_product_by_name(product.name)
        movement: StockMovement

        if stock_product:    
            product_movement = Product(stock_product.id, stock_product.name, product.quantity)
            movement = StockMovement(product_movement, product.date, product.operator)
            stock_product.quantity += product.quantity
            self.update_product(stock_product)
        else:
            next_id: int = self.__products[-1].id + 1 if len(self.__products) > 0 else 1
            new_product: Product = Product(next_id, product.name, product.quantity)
            movement = StockMovement(new_product, product.date, product.operator)
            self.__products.append(new_product)
        self.__history.add_history(movement)
    
    def withdraw_product(self, product: WithdrawProductDTO) -> Product:
        stock_product = self.get_product_by_id(product.id)

        if(stock_product is None):
            raise ValueError("Não há um produto com esse ID")

        if(product.quantity > stock_product.quantity):
            raise ValueError("Estoque insuficiente para realizar esta operação")
        
        stock_product.quantity = stock_product.quantity - product.quantity
        self.update_product(stock_product)

        return stock_product

        




