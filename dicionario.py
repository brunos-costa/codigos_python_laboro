agenda = {"Maria":1234,"Pedro":4321,"Joana":9876}
contato = {"nome":"Claudio", "Idade":45}

print(type(agenda))

print(agenda)

print("-"*40)
print(agenda["Maria"])#mostrar o conteúdo da chave
print(f"Nome: {contato["nome"]} Idade: {contato['Idade']}")

# INSERINDO DADOS NA AGENDA
#Forma 1
agenda["José"] = 1145

print(agenda)

#Forma 2
#Update pode inserir um novo valor ou alterar um já existente
agenda.update({"Claudia":2222})
print(agenda)

# EXCLUINDO DADOS DA AGENDA
#Forma 1
agenda.pop("Pedro")
print(agenda)

#Forma 2
del agenda["Maria"]
print(agenda)

