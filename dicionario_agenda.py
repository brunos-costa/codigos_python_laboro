agenda = dict()# inicializando um dicionário

# Função Menu
def menu():
    print("\nAgenda Eletrônica\n")
    print("1- Inserir dados na agenda")
    print("2- Excluir dados da agenda")
    print("3- Consultar todos os dados da agenda")
    print("4- Sair do sistema")

# Função inserir dados
def inserir():
    try:
        nome = input("Qual o nome do contato: ")
        agenda[nome] = int(input(f"Qual o número de {nome}: "))
            
        print("Contato inserido com sucesso!")
        print(agenda)

    except Exception:
        print("Operação inválida. Contato não salvo.")


# Função excluir dados
def excluir(escolha):
    # Verificando se o contato existe antes de excluir
    if escolha in agenda:        
        del agenda[escolha]
        print("Dado excluído com sucesso!")
        print(agenda)

    else:
        print(f"O contato {escolha} não existe na agenda")

# Função consultar dados
def consultar():
    for chave, valor in agenda.items():
        print(f"{chave} : {valor}")



while True:
    menu()
    resposta = int(input("Qual sua escolha: "))

    if resposta == 1:
        inserir()
        
    elif resposta == 2:
        print(agenda)
        escolha = input("Qual o nome do contato para excluir: ")

        excluir(escolha)      
       
    elif resposta == 3:
        consultar()

    elif resposta == 4:
        print("Sistema Encerrado")
        break