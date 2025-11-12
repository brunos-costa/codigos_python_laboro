# Contagem com recursividade
def contagem(num):

    if num >= 1:
        print(num)
        num =num - 1
        contagem(num)

#chamando a função
contagem(10)