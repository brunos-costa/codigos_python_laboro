import os

def menu():
    print("--- MENU ---")
    print("1. Consultar")
    print("2. Inserir")
    print("3. Excluir")
    print("4. Sair")

lista = []# criando uma lista vazia

while True:
    menu()
    resposta = int(input("Qual sua escolha: "))

    if resposta == 1:
        if os.path.exists("funcionario.txt"):
            with open("funcionario.txt","r",encoding="utf-8") as arquivo:

                # armazenando todo o arquivo em uma lista
                lista = arquivo.readlines()

                for indice,itens in enumerate(lista):
                    print(f"{indice}- {itens}",end="")

    elif resposta == 2:

        with open("funcionario.txt","a",encoding="utf-8") as arquivo:
            
            dado = input("Informe o nome do funcionário: ")

            arquivo.write(dado + "\n")

            print("Dado inserido com sucesso")
    
    elif resposta == 3:
        #abrindo o arquivo em modo leitura
        with open("funcionario.txt","r",encoding="utf-8") as arquivo:
            lista =arquivo.readlines()

        # abrindo o arquivo em modo escrita
        with open("funcionario.txt","w",encoding="utf-8") as arquivo:
            
            dado = int(input("Informe o número do funcionário: "))

            lista.pop(dado)

            arquivo.writelines(lista)








    elif resposta == 4:
        break