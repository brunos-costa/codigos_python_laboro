ARQUIVO = "agenda.txt"

# Função carregar dados do arquivo
def carregar():
    dados = dict()
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()# remove os espaços e quebras de linha que estão no começo e no fim de um texto.
                if linha:  # ignora linhas vazias
                    nome, numero = linha.rsplit(":", 1) #Essa linha divide o texto em duas partes e guarda cada parte em uma variável. 

                    """
                        nome, numero =linha.rsplit(":", 1) : Essa linha divide o texto em duas partes e guarda cada parte em uma variável.

                        Pegando a linha "Maria:998877665":
                        
                        nome, numero = linha.rsplit(":", 1) -> rsplit: significa: “separe o texto pelo :, mas só uma vez, começando pela direita”.

                        Resultado:

                        nome   = "Maria"
                        numero = "998877665"
                    """
                    dados[nome] = int(numero)
    except FileNotFoundError:
        pass  # primeira execução: começa com a agenda vazia
    return dados

# Função salvar dados no arquivo
def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for nome, numero in agenda.items():
            f.write(f"{nome}:{numero}\n")


agenda = carregar()  # em vez de dict(), já carrega o que estava salvo

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
        salvar()  # grava no arquivo

        print("Contato inserido com sucesso!")
        print(agenda)

    except Exception:
        print("Operação inválida. Contato não salvo.")


# Função excluir dados
def excluir(escolha):
    # Verificando se o contato existe antes de excluir
    if escolha in agenda:
        del agenda[escolha]
        salvar()  # atualiza o arquivo
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