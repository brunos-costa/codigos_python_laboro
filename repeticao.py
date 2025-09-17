"""
for(etapa1; etapa2; etapa3){

}
"""
# range() não conta o valor final, ele ignora. Se eu quiser exibir o valor final devo colocar ele + 1

# EXEMPLO 1
for contador in range(1,11):
    print(contador)


print("-" * 20)

# EXEMPLO 2
#O -1 indica que o intervalo irá de -1 em -1,isto é o passo a passo do valor inicial até o valor final. 
for contador in range(10,0,-1):
    print(contador,end=" ")

print("\n")
print("-" * 20)

#EXEMPLO 3
for contador in range(0,21,2):
    print(contador, end=", ")
