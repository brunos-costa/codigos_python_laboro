alimentos = {"Arroz":5.99,"Café":14,"Feijão":7.69}

"""
Dicionário
chave: valor -> item

chave - key
valor - value
item  - item

"""
print(alimentos)

# ACESSANDO APENAS AS CHAVES
for chave in alimentos.keys():
    print(chave)

# ACESSANDO APENAS OS VALORES
for valor in alimentos.values():
    print(valor)

# ACESSANDO TANTO A CHAVE QUANTO VALOR
for chave, valor in alimentos.items():
    print(f"{chave} : {valor}")