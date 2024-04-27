###################################################
#MC102 - Algoritmos e Programação de Computadores
#Laboratório 5 - Dados da Sorte
#Nome: Fernanda Elias
#RA: 259427
###################################################

def ContadorMuitoFoda(dado_1, limiteinferior, limitesuperior):
    contador_yey = 0

    for dado_2 in range(1,7):
        for dado_3 in range(1,7):
            for dado_4 in range(1,7):
                if (dado_1 != dado_2 and
                    dado_1 != dado_3 and
                    dado_1 != dado_4 and
                    dado_2 != dado_3 and
                    dado_2 != dado_4 and
                    dado_3 != dado_4):
                    sum = dado_1 + dado_2 + dado_3 + dado_4
                    if limiteinferior <= dado_1 + dado_2 + dado_3 + dado_4 <= limitesuperior:
                        contador_yey += 1
    return contador_yey


#Leitura da entrada de dados
dado_1 = int(input())
limite_inferior = int(input())
limite_superior = int(input())

#Processamento dos casos de ativação do bônus
#Saída de dados
print(f"{ContadorMuitoFoda(dado_1, limite_inferior, limite_superior)} de 216 combinações podem ativar o bônus")