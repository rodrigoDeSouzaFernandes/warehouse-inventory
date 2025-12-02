from datetime import datetime
from validations import is_valid_date, is_valid_quanity

# Códigos ANSI para cores
ERROR = "\033[91m"
SUCCESS = "\033[92m"
ALERT = "\033[93m"
RESET = "\033[0m"

def input_text(message:str) -> str:
    name = input(f"\n{message}:\n\n>>>")
    while(len(name) < 2):
        print(f"{ALERT}O campo deve ter pelo menos 2 caracteres{RESET}")
        name = input(f"{message}:\n\n>>>")
    return name

def input_int(message:str) -> int:
    quantity = input(f"\n{message}:\n\n>>>")
    while(not is_valid_quanity(quantity)):
        print(f"{ALERT}Informe um número inteiro, positivo e maior que zero (0){RESET}")
        quantity = input(f"{message}:\n\n>>>")
    return int(quantity)

def input_date():
    converted_date = datetime.today()
    date = input("\nInforme a data da entrada (dd/mm/yyyy):\n[Pressione enter sem digitar qualquer dado para prosseguir com a data atual]\n>>>")

    while(True):
        if(date == ""):
            return datetime.today() 
        try:
            converted_date = datetime.strptime(date, "%d/%m/%Y")
            break
        except:
            print(f"\n{ERROR}Erro: Data inválida{RESET}")    
            date = input(f"{ALERT}Entre com o campo vazio para data de hoje, ou informe uma data no formato \"dd/mm/yyyy\"{RESET}\n>>>")  
    return converted_date

# Limpa o console usando códigos ANSI (move cursor e apaga a tela)
def clear_console():
    print("\033c", end="")

