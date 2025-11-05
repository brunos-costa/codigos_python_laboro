def verificaParImpar():
    resposta = int(input("Informe um valor:"))

    if resposta % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
# chamando a função

print(f"O valor digitado é {verificaParImpar()}")