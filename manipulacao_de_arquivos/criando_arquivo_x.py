# Trabalhando com o modo:
# 'x' -> cria arquivo e exibe erro caso exista
try:
    arquivo = open("legumes.txt","x")

    arquivo.write("Tomate\n")
    arquivo.write("Alface\n")


    arquivo.close()
    
except Exception:
    print("Não foi possível criar o arquivo,ele já existe")