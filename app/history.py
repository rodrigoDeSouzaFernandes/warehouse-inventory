from models import  StockMovement

class History:
    def __init__(self):
        self.__history: list[StockMovement] = []

    def get_history(self, range: int) -> list[StockMovement]:
        return self.__history[-range:]
    
    def add_history(self, movement: StockMovement) -> None:
        self.__history.append(movement)