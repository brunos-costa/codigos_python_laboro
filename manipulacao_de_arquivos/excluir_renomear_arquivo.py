import os

#Renomear
#os.rename("nome_antigo","nome_novo")
#os.rename("livro.txt","biblioteca.txt")

# Verificar se o arquivo existe

if os.path.exists("biblioteca.txt"):
    os.remove("biblioteca.txt")
    print("Arquivo apagado com sucesso - 200")
else:
    print("Arquivo não encontrado - 404")