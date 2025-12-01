from dataclasses import dataclass
from datetime import datetime
from enum import Enum


@dataclass
class Product:
    id: int
    name: str
    quantity: int

@dataclass
class AddProductDTO:
    name: str
    quantity: int
    operator: str
    date: datetime

class Operation(Enum):
    ADD = "Adição"
    REMOVE = "Remoção"

@dataclass
class StockMovement:
    product: Product
    date: datetime
    operator: str
    operation: Operation

@dataclass
class WithdrawProductDTO:
    id: int
    quantity:int
    operator: str