from dataclasses import dataclass
from datetime import datetime

@dataclass
class Product:
    id: int
    name: str
    quantity: int

@dataclass
class AddProductDTO:
    name: str
    quantity: int
    date: datetime
    operator: str

@dataclass
class StockMovement:
    product: Product
    date: datetime
    operator: str