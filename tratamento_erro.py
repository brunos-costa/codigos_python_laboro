try:
    valor = int(input("Informe um valor numérico: "))
    print(f"O número digitado foi {valor}")

except Exception as erro:
    print(f"Coisa feia,tentando colocar texto no lugar de números. O erro foi : {erro}")


