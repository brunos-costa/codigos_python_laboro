# Trabalhando com o modo:
#'w' -> escreve(substitui) / cria arquivo


arquivo = open("frutas.txt","w")

# verificando se um arquivo pode ser escrito
print(arquivo.writable())
arquivo.write("Maracuja\n")
arquivo.write("Acerola\n")
arquivo.write("Uva\n")
arquivo.write("Manga\n")


arquivo.close()

# Criando outro arquivo
arquivo = open("verduras.txt","w")
arquivo.write("Batata\n")
arquivo.write("Cenoura\n")
arquivo.write("Maxixe\n")
arquivo.write("Quiabo\n")
# Escrevendo várias linhas
arquivo.writelines(["Macaxeira\n","Beterraba\n"])


arquivo.close()