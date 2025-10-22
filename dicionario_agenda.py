agenda = dict()# inicializando um dicionário

while True:
    print("\nAgenda Eletrônica\n")
    print("1- Inserir dados na agenda")
    print("2- Excluir dados da agenda")
    print("3- Sair do sistema")
    resposta = int(input("Qual sua escolha: "))

    if resposta == 1:
        nome = input("Qual o nome do contato: ")
        agenda[nome] = int(input(f"Qual o número de {nome}: "))
        
        print("Contato inserido com sucesso!")
        print(agenda)

    elif resposta == 2:
        print(agenda)
        escolha = input("Qual o nome do contato para excluir: ")
        
        # Verificando se o contato existe antes de excluir
        if escolha in agenda:        
            del agenda[escolha]
            print("Dado excluído com sucesso!")
            print(agenda)

        else:
            print(f"O contato {escolha} não existe na agenda")
        


    elif resposta == 3:
        print("Sistema Encerrado")
        break