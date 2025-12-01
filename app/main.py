from stock import Stock
from history import History
from models import AddProductDTO

from datetime import datetime

from validations import is_valid_quanity, is_valid_date

# Códigos ANSI para cores
ERROR = "\033[91m"
SUCCESS = "\033[92m"
ALERT = "\033[93m"
RESET = "\033[0m"

history = History()
stock = Stock(history)

menuOptions = {
    "1": "Buscar um produto por Id",
    "2": "Listar todos os produtos",
    "3": "Registrar novo produto",
    "4": "Atualizar um produto existente",
    "5": "Excluir um produto",
    "6": "Imprimir histórico recente de movimentações",
}

def print_menu_options():
    print("")
    for key in menuOptions:
        print(f"{key} - {menuOptions[key]}")
    print("\n0 - SAIR\n")
    
option = ""

def input_name() -> str:
    name = input("Informe o nome do produto:\n>>>")
    while(len(name) < 5):
        print(f"{ALERT}O nome do produto deve ter pelo menos 5 caracteres{RESET}")
        name = input("Informe o nome do produto:\n>>>")
    return name

def input_quantity():
    quantity = input("Informe a quantidade:\n>>>")
    while(not is_valid_quanity(quantity)):
        print(f"{ALERT}A quantidade deve ser um número inteiro, positivo e maior que zero (0){RESET}")
        quantity = input("Informe a quantidade:\n>>>")
    return quantity

def input_date():
    date = input("Informe a data da entrada (dd/mm/yyyy):\n[Pressione enter sem digitar qualquer dado para prosseguir com a data atual]\n>>>")
    while(not is_valid_date(date)):
        if(date == ""):
            return datetime.today()
        date = input(f"{ALERT}Entre com o campo vazio para data de hoje, ou informe uma data no formato \"dd/mm/yyyy\"{RESET}\n>>>")
        
        try:
            date = datetime.strptime(date, "%d/%m/%Y")
        except:
            print(f"{ERROR}Insira uma data válida{RESET}")
            date = None    
    return date

def add_product():
    name = input_name()
    quantity = input_quantity()
    date = input_date()

    print(name)
    print(quantity)
    print(date)

    
    


date = input_date()
print(date)    

isRunning = False

while(isRunning):
    print("---- SISTEMA DE ESTOQUE ----")
    print_menu_options()
    option = input("Selecione a opção desejada:\n>>>")

    match option:
        case "0":
            print("\nPrograma encerrado\n")
            isRunning = False
            break
            
