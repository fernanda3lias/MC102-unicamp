###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Em Busca de um Chuveiro
# Nome: Fernanda 
###################################################

# Leitura da entrada
resistencia = int(input())
tensao  = int(input())
horas = int(input())
custo = float(input()) # reais do kWh
limite = int(input())

# Cálculo do consumo e impressão da saída
potencia = ((tensao ** 2) / resistencia)

consumo = ((potencia * horas) / 1000) #kWh

custo = custo * consumo


if custo <= limite:
    print (True)

else:
    print(False)


