from stock import Stock
from history import History
from models import AddProductDTO, WithdrawProductDTO

from helpers import ERROR, SUCCESS, ALERT, RESET, input_text, input_int, input_date, clear_console

history = History()
stock = Stock(history)

isRunning = True
operator = ""

menuOptions = {
    "1": "Listar todos os produtos",
    "2": "Buscar um produto",
    "3": "Adicionar um produto",
    "4": "Retirar um produto",
    "5": "Imprimir histórico recente de movimentações",
}

def print_menu_options():
    print("")
    for key in menuOptions:
        print(f"{key} - {menuOptions[key]}")
    print("\n0 - SAIR\n")

def add_product():
    clear_console()
    print("----- Adicionar Produto -----")
    name = input_text("Informe o nome do produto")
    quantity = input_int("Informe a quantidade")
    date = input_date()

    new_product = AddProductDTO(
        name,
        quantity,
        operator,
        date=date,
    )

    stock.add_product(new_product)
    print(f"\n{SUCCESS}{quantity} unidade(s) do produto \"{name}\" adicionada(s) ao estoque\n{RESET}")
    input("Pressione ENTER para retornar")

def remove_product():
    clear_console()
    print("----- Retirar Produto -----")
    id = input_int("Informe o ID do produto a ser retirado")
    quantity = input_int("Informe a quantidade a ser retirada")

    product = WithdrawProductDTO(
        id,
        quantity,
        operator
    )

    try:
        product = stock.withdraw_product(product)
        print(f"\n{SUCCESS}Foram retiradas {quantity} unidade(s) do produto \"{product.name}\" do estoque\n{RESET}")
    except ValueError as error:
        print(f"\n{ERROR}{str(error)}\n{RESET}")
    input("Pressione ENTER para retornar ao menu inicial")


def list_all_products():
    clear_console()
    print("----- Listagem de Produtos -----")
    products = stock.get_products()
    print(f"{"ID":<5} | {"Nome":<20} | {"Quantidade":<5}")

    for product in products:
        print(f"{product.id:<5} | {product.name:<20} | {product.quantity:<5}")
    
    print(f"\nTotal de produtos encontrados: {len(products)}\n")
    input("Pressione ENTER para retornar ao menu inicial\n")

def get_product_by_id():
    clear_console()
    print("----- Buscar Produto por ID -----")
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

def find_products_by_name():
    clear_console()
    print("----- Buscar Produtos por Nome -----")

    name = input_text("Informe o nome ou parte do nome do produto")
    products = stock.get_products_by_name(name)
    clear_console()
    if len(products) > 0:
        print(f"Produtos com \"{name}\" no nome:\n")
        print(f"{"ID":<5} | {"Nome":<20} | {"Quantidade":<5}")
        for product in products:
            print(f"{product.id:<5} | {product.name:<20} | {product.quantity:<5}")
    else:
        print(f"\n{ERROR}Não foi encontrado nenhum produto contendo \"{name}\" no nome{RESET}")

    input("\nPressione ENTER para retornar\n")

            
def get_product():
    while(True):
        clear_console()
        print("----- Buscar Produto -----")
        option = input("\nDeseja buscar por:\n\n1 - Id   [Retorna um produto]\n2 - Nome [Retorna uma lista]\n\n0 - Voltar\n\n>>>")
        match option:
            case "1":
                get_product_by_id()
            case "2":
                find_products_by_name()
            case "0":
                break
            case _:
                print(f"{ALERT}\nEscolha uma das opções a seguir:{RESET}")

def get_history():
    clear_console()
    print("----- Histórico de Movimentações -----")
    history = stock.get_history()

    if len(history) > 0:
        print(f"\n{"Produto":<20} | {"Quantidade":<10} | {"Operação":<10} | {"Operador":<10} | {"Data":<10}")
        for item in history:
            print(f"{item.product.name:<20} | {item.product.quantity:<10} | {item.operation.value:<10} | {item.operator:<10} | {item.date.strftime("%d/%m/%Y %H:%M"):<20} ")
    else:    
        print(f"{ALERT}Histórico vazio, ainda não houveram movimentações{RESET}")
    
    input("\nPressione ENTER para retornar\n")

while(True):
    print("----- SISTEMA DE ESTOQUE -----")
    operator = input_text("Informe o seu nome")
    print(f"{ALERT}\nSeu nome é {operator}{RESET}")
    option = input("\n1 - Confirmar\n0 - Alterar\n\n>>>")

    match option:
        case "1": break
        case "0": pass
        case _: print("teste")

while(isRunning):
    clear_console()
    print("----- SISTEMA DE ESTOQUE -----")
    print_menu_options()
    option = input("Selecione a opção desejada:\n\n>>>")

    match option:
        case '1':
            list_all_products()
        case "2":
            get_product()
        case "3":
            add_product()
        case "4":
            remove_product()
        case "5":
            get_history()
        case "0":
            print("\nPrograma encerrado\n")
            isRunning = False
            break
            
