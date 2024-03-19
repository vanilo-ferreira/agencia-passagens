def mostra_menu():
    print("==" * 50)
    print("Escolha uma das opções abaixo:")
    print("Digite 1 para comprar passagens")
    print("Digite 2 para listar passagens")
    print("Digite 3 para sair do programa")
    print("==" * 50)
    print()
    
def menu_compra_passagem():
    print("Você escolheu comprar passagens")
        
    origem = input("Qual a origem? ")
    destino = input("Qual o destino? ")
    preco = float(input("Qual o preco? "))
    return(origem, destino, preco)