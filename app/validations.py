from datetime import datetime

def isIntegerPositive(value: str) -> bool:
    try:
        num = float(value)
        return num.is_integer() and num >= 0
    except ValueError:
        return False
    
def is_valid_quanity(value: str) -> bool:
    return isIntegerPositive(value) and value != "0"

def is_valid_date(value: str) -> bool:
    try:
        datetime.strptime(value, "%d/%m/%Y")
        return True
    except Exception as err:
        return False