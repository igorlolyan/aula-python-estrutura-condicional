valores = input().split() 

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
hot_dogs = int(valores[0])
people = int(valores[1])
media = hot_dogs / people
print('{:.2f}'.format(média))