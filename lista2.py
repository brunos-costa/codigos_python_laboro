valores = [] # criando uma lista vazia

for item in range(10,14):
    valores.append(item)

print(valores)

# Preenchedo uma lista com dados dinâmicos
valores2 = []
while True:
    num = int(input("Informe um valor númerico qualquer - zero para encerrar: "))

    if num == 0:
        break #encerra o sistema
    else:
        valores2.append(num)

print("\nPrograma encerrado\n")
print(valores2)

while True:
    print(valores2)

    print("Deseja apagar? 1-sim 2-não")
    resposta = int(input("Qual sua resposta? "))

    #len() irá verificar o tamanho da lista.
    if len(valores2)<=0:
        print("Lista vazia")
        break
    elif resposta == 1:
        valores2.pop()
    elif resposta==2:
        break

