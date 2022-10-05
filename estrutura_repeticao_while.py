opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

# Repetição infinita até atingir a condição. Pode colocar True ou 1 == 1
while True:
    numero = int(input("informe um número: "))

    if numero % 2 == 0:
        print("Número par digitado. Encerrando prorama...")
        break

    print(numero)
