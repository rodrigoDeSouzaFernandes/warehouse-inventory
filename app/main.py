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
    "4": "Excluir um produto",
    "5": "Imprimir histórico recente de movimentações",
}

def print_menu_options():
    print("")
    for key in menuOptions:
        print(f"{key} - {menuOptions[key]}")
    print("\n0 - SAIR\n")
    
option = ""

def input_text(message:str) -> str:
    name = input(f"{message}:\n>>>")
    while(len(name) < 2):
        print(f"{ALERT}O campo deve ter pelo menos 2 caracteres{RESET}")
        name = input(f"{message}:\n>>>")
    return name

def input_int(message:str) -> int:
    quantity = input(f"{message}:\n>>>")
    while(not is_valid_quanity(quantity)):
        print(f"{ALERT}Informe um número inteiro, positivo e maior que zero (0){RESET}")
        quantity = input(f"{message}:\n>>>")
    return int(quantity)

def input_date():
    date = input("Informe a data da entrada (dd/mm/yyyy):\n[Pressione enter sem digitar qualquer dado para prosseguir com a data atual]\n>>>")
    while(not is_valid_date(date)):
        if(date == ""):
            return datetime.today()
        print(f"{ERROR}Erro: Data inválida{RESET}")
        date = input(f"{ALERT}Entre com o campo vazio para data de hoje, ou informe uma data no formato \"dd/mm/yyyy\"{RESET}\n>>>")       
        try:
            date = datetime.strptime(date, "%d/%m/%Y")
        except:
            date = None    
    return date

def add_product():
    name = input_text("Informe o nome do produto")
    quantity = input_int("Informe a quantidade")
    date = input_date()

    new_product = AddProductDTO(
        name,
        quantity,
        operator="Rodrigo",
        date=date,
    )

    stock.add_product(new_product)
    print(f"\n{SUCCESS}{quantity} unidade(s) do produto \"{name}\" adicionada(s) ao estoque\n{RESET}")

def remove_product():
    id = input_int("Informe o ID do protudo a ser excluído")

    


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
            
