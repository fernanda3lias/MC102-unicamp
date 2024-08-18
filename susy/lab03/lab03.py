###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Cupons de Desconto
# Nome: Fernanda
###################################################

# leitura de dados
X1 = int(input())
Z1 = int(input())
X2 = int(input())
Z2 = int(input())
X3 = int(input())
Z3 = int(input())
Valor = int(input())

# cálculo dos descontos
Cupom1 = False
Cupom2 = False 
Cupom3 = False
Desconto1 = 0
Desconto2 = 0
Desconto3 = 0

if Valor >= Z1:
    Cupom1 = True
    Desconto1 = X1
    # X1 reais de desconto

if Valor:
    Cupom2 = True
    Desconto2 = Valor * (X2/100)

    if Desconto2 > Z2:
        Desconto2 = Z2

if Valor >= Z3:
    Cupom3 = True
    Desconto3 = Valor * (X3/100)
    
Descontos = [Desconto1, Desconto2, Desconto3]

Maior_desconto = max(Descontos)
Indices = []

for i, j in enumerate(Descontos):
    if j == Maior_desconto:
        Indices.append(i + 1)

if len(Indices) == 1:
    print(f"Maior desconto: Cupom {Indices[0]}")

elif len(Indices) >= 2:
    print(f"Maior desconto: Cupons {str(Indices).replace(']', '').replace('[', '')}")
    

# Impressão da saída

# ...
print("Valor do desconto: R$ {:.2f}".format(Maior_desconto).replace(".", ","))
