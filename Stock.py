from models import Product, StockMovement, AddProductDTO

class Stock:
    def __init__(self):
        self.__products: list[Product] = []
        self.__history: list[StockMovement]

    def get_product_by_name(self, name:str) -> Product | None:
        return next((p for p in self.__products if p.name == name), None)
    
    def get_product_by_id(self, id:int) -> Product | None:
        return next((p for p in self.__products if p.id == id), None)

    def add_product(self, movement:StockMovement) -> None:
        product_exists: Product = self.get_product_by_name(movement.product.name)

        