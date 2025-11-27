#Criar Arquivo - modo 'w'

#encoding="utf-8" indica que o arquivo irá aceitar caracteres especiais como: acentos, cedilhas, etc
with open("livro.txt","w",encoding="utf-8") as livro:
    livro.write("100 anos de solidão\n")
    livro.write("Noites Brancas\n")
    livro.write("Damas das Camélias\n")


# Consultando dados do arquivo
with open("livro.txt","r", encoding="utf-8") as livro:
    print(livro.read())