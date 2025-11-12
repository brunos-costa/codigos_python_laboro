valor = 50

def mensagem():
    global valor #Declara que estamos usando a variável que está fora da função (global)

    print(f"Exibindo a variável valor: {valor}")

    valor = valor + 10
    print(f"Valor da variável atualizada: {valor}")

# chamando função
mensagem()