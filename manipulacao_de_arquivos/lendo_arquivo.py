# Vamos abrir um arquivo

'''
r -> modo de leitura

'''

#abrindo umarquivo em modo de leitura 
arquivo = open("frutas.txt","r")

# Verificando se um arquivo pode ser lido

print(arquivo.readable())


#print(arquivo.read())# Lendo o conteúdo de um arquivo

# Lendo apenas 1 linha do arquivo
#print(arquivo.readline())

#Lendo várias linhas
resultado = arquivo.readlines()
print(resultado) 


arquivo.close()# fechandoo arquivo