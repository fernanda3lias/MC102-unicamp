###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 06 - Espectativa de Vendas Mensais
# Nome: Fernanda Elias
# RA: 259427
###################################################

# Leitura da quantidade de meses e os valores de vendas mensais
N = int(input())
vendas = []
meses = []

for i in range(N):
    vendas.append(float(input()))
    meses.append(i+1)


# Verificação das expectativas de mensais de vendas
sum_xivi = 0
sum_xi = 0
sum_vi = 0
sum_xi2 = 0
sum2_xi = 0
n = 0

for i in meses:
    if i > 2:
        sum2_xi = (sum_xi) ** 2
        n = i-1

        m = ((n * sum_xivi) - (sum_xi * sum_vi))/((n * sum_xi2) - sum2_xi)
        b = (sum_vi - (m * sum_xi))/(n)

        x = i 
        reta = m * x + b

        if reta == vendas[i-1]:
            print(vendas[i-1], round(reta,1), "ESPERADO")

        if reta < vendas[i-1]:
            print(vendas[i-1], round(reta,1), "SUPERIOR")

        if reta > vendas[i-1]:
            print(vendas[i-1], round(reta, 1), "INFERIOR")

    xivi = i * vendas[i-1]
    sum_xivi += xivi
    sum_xi += i
    sum_vi += vendas[i-1]
    sum_xi2 += (i) ** 2

