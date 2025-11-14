from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    quantity: int

@dataclass
class StockMovement:
    product: Product
    date: datetime
    operator: str


class Stock:
    def __init__(self):
        self.__products: list[Product] = []
        self.__history: list[StockMovement]

    def get_product_by_name(self, name:str) -> Product | None:
        return next((p for p in self.__products if p.name == name), None)
    
    def get_product_by_id(self, id:int) -> Product | None:
        return next((p for p in self.__products if p.id == id), None)
