from passagem import Passagem, PassagensAereasManager
from apresentacao import menu_compra_passagem, mostra_menu

while True:
    passagens_aereas_manager = PassagensAereasManager()
    # Mostrar o menu para o usuário com as opções 
    
    mostra_menu()  

    #Receber a entrada do usuário
    entrada_do_usuario = int(input())
    
    if entrada_do_usuario == 1:
        origem, destino, preco = menu_compra_passagem()
        passagem = Passagem(origem, destino, preco)
        passagens_aereas_manager.adicionar_passagem(passagem)
        
    elif entrada_do_usuario == 2:
        # lista_passagens(passagens_aereas_manager.passagens_compradas)
        # lista_passagens(PassagensAereasManager.listar_passagens())
        for indice, passagem in enumerate(passagens_aereas_manager.passagens_compradas):
            print(f"{indice+1} {passagem}")

    # Se o usuário escolher sair do progrma, usar break para encerrar o programa
    elif entrada_do_usuario == 3:
        print("Encerrando o programa, volte sempre! ")
        break