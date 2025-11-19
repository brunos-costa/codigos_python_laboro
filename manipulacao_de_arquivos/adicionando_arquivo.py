# Trabalhando com o modo:
# 'a'->(append) adiciona conteúdo no final do arquivo 

# abrindo o arquivo em modo de escrita 
arquivo = open("frutas.txt","a")

arquivo.write("Goiba\n")
arquivo.write("Jambo\n")
arquivo.write("Pitanga\n")


arquivo.close()