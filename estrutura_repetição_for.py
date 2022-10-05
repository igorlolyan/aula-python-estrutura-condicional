texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()   # adiciona uma quebra de linha


# Exemplo utilizando a função built-in range
for numero in range (0, 51, 5):
    print(numero, end= " / ")     # sem nada da quebra de linha e com end = "" fica o texto escolhido a cada print.