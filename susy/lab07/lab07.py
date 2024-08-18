###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Montanha Russa
# Nome: Fernanda
###################################################

# Leitura de dados
N = int(input())
values = []

for i in range(N):
    val = float(input())
    values.append(val)

budget = float(input())

max_profit = 0
buy_day = 0

# Cálculo dos dias de compra e venda
for i in range(len(values)):
    D1 = values[i]
    for j in range(len(values)):
        if j > i:
            D2 = values[j]
            for k in range(len(values)):
                if k > j:
                    D3 = values[k]
                    for l in range(len(values)):
                        if l > k:
                            D4 = values[l]
                            div = int(budget/D1) #Tenho isso de ações primeiro dia
                            rest = budget % D1 #Sobra isso de dinheiro

                            profit = div * D2  + rest

                            div2 = int(profit/ D3)
                            rest2 = profit % D3

                            profit2 = (div2 * D4) + rest2
                            if profit2 > max_profit:
                                max_profit = profit2
                                venda = profit2
                                dia1 = D1
                                dia2 = D2
                                dia3 = D3
                                dia4 = D4

                                valor_d1 = i+1
                                valor_d2 = j+1
                                valor_d3 = k+1
                                valor_d4 = l+1
                                

# Impressão da saída
print("Dia da primeira compra:", valor_d1)
dia1= float(dia1)
dia1 = f"{dia1:,.2f}"
dia1 = dia1.replace(".", ",")
print(f"Valor de compra: R$ {dia1}")
print("Dia da primeira venda:", valor_d2)
dia2 = float(dia2)
dia2 = f"{dia2:,.2f}"
dia2 = dia2.replace(".", ",")
print(f"Valor de venda: R$ {dia2}")
print("Dia da segunda compra:", valor_d3)
dia3 = f"{dia3:,.2f}"
dia3 = dia3.replace(".", ",")
print(f"Valor de compra: R$ {dia3}")
print("Dia da segunda venda:", valor_d4)
dia4 = f"{dia4:,.2f}"
dia4 = dia4.replace(".", ",")
print(f"Valor de venda: R$ {dia4}")
venda = round(venda, 2)
venda = f"{venda:.2f}"
venda = venda.replace(".", ",")
print(f"Valor final: R$ {venda}")