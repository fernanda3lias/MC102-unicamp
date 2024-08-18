###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Dados da Sorte
# Nome: Fernanda
###################################################

# Leitura da entrada de dados
dado_1 = int(input())
limite_inferior = int(input())
limite_superior = int(input())

# Processamento dos casos de ativação do bônus
counter = 0

dados_range = range(limite_inferior, limite_superior + 1)

for i in range(1,7):
    if i != dado_1:
        for j in range(1, 7):
            for k in range(1, 7):
                if j != i and j != dado_1:
                    if k != j and k != i and k != dado_1: 
                        sum = dado_1 + i + j + k

                        if sum in dados_range:
                            counter += 1

# Saída de dados
print(f"{counter} de 216 combinações podem ativar o bônus")