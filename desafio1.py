# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
distancia = int(input())
diametro1 = int(input())
diametro2 = int(input())
icm = distancia / (diametro1 + diametro2)
print('{:.2f}'.format(icm))                                    #print(f'{icm:.2f}')    # print("%.2f" % icm) também funciona