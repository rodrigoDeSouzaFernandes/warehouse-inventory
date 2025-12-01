import re
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
    date_pattern = r"^\d{2}\/\d{2}\/\d{4}$"
    date_str = re.match(date_pattern, value)
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except:
        return False