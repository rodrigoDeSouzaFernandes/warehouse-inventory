from stock import Stock
from history import History
from models import AddProductDTO, WithdrawProductDTO

from helpers import ERROR, SUCCESS, ALERT, RESET, input_text, input_int, input_date, clear_console



history = History()
stock = Stock(history)

menuOptions = {
    "1": "Listar todos os produtos",
    "2": "Buscar um produto por Id",
    "3": "Adicionar um produto",
    "4": "Retirar um produto",
    "5": "Imprimir histórico recente de movimentações",
}

def print_menu_options():
    print("")
    for key in menuOptions:
        print(f"{key} - {menuOptions[key]}")
    print("\n0 - SAIR\n")
    
option = ""



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
    id = input_int("Informe o ID do produto a ser excluído")
    quantity = input_int("Informe a quantidade")

    product = WithdrawProductDTO(
        id,
        quantity
    )

    try:
        stock.withdraw_product(product)
    except ValueError as error:
        print(f"\n{ERROR}{str(error)}\n{RESET}")
        input("Pressione ENTER para retornar ao menu inicial\n")


def list_all_products():
    products = stock.get_products()
    print(f"{"ID":<5} | {"Nome":<20} | {"Quantidade":<5}")

    for product in products:
            print(f"{product.id:<5} | {product.name:<20} | {product.quantity:<5}")
    
    print(f"\nTotal de produtos encontrados: {len(products)}\n")
    input("Pressione ENTER para retornar ao menu inicial\n")

def get_product_by_id():
    id = input_int("Informe o ID do produto")
    product = stock.get_product_by_id(id)
    if product is None:
        print(f"{ERROR}Nenhum produto com este ID foi encontrado{RESET}")
    else:
        clear_console()
        print("----------------------")
        print(f"ID: {product.id}")
        print(f"Nome: {product.name}")
        print(f"Quantidade: {product.quantity}")
        print("----------------------")
    input("Pressione ENTER para retornar\n")

def get_products_by_name():
    name = input_text("Informe o nome ou parte do nome do produto")

            
def get_product():
    clear_console()
    while(True):
        option = input("\nDeseja buscar o produto por:\n\n1 - Nome\n2 - Id\n\n0 - Voltar\n\n>>>")
        match option:
            case "1":
                print('implementar')
            case "2":
                get_product_by_id()
            case "3":
                break
            case _:
                print(f"{ALERT}Escolha uma das opções acima{RESET}")
    


isRunning = True

while(isRunning):
    print("---- SISTEMA DE ESTOQUE ----")
    print_menu_options()
    option = input("Selecione a opção desejada:\n>>>")

    match option:
        case '1':
            list_all_products()
        case "2":
            get_product()
        case "3":
            add_product()
        case"4":
            remove_product()
        case "0":
            print("\nPrograma encerrado\n")
            isRunning = False
            break
            
