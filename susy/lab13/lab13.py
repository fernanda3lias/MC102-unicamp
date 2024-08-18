###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Transporte de Itens
# Nome: Fernanda
###################################################

# Leitura da capacidade e quantidade de itens
capacidade = int(input())
n = int(input())

# Leitura dos itens, pesos e valores
itens = []
pesos = []
valores = []


for i in range(n):
    item, peso, valor = input().split()
    peso = int(peso)
    valor = int(valor)
    itens.append(item)
    pesos.append(peso)
    valores.append(valor)

copia_itens = itens.copy()
copia_pesos = pesos.copy()
copia_valores = valores.copy()


dict_pesos = {}
for i in range(len(itens)):
    dict_pesos[itens[i]] = [pesos[i], valores[i]]


valor_por_peso, valor_por_valor, valor_por_razao = 0, 0, 0
carregado_por_peso, carregado_por_valor, carregado_por_razao = 0, 0, 0


# Ordenação por peso
def ordenar_valor(lista, valores):
    n = len(lista)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lista[j] < lista[j + 1]:
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
                (valores[j], valores[j + 1]) = (valores[j + 1], valores[j])


ordenar_valor(pesos, valores)

carregado_por_peso = 0
valor_por_peso = 0
for i in range(n):
    item = pesos[i]
    if carregado_por_peso + item <= capacidade:
        carregado_por_peso += item
        valor_por_peso += valores[i]

# Ordenação por valor
ordenar_valor(valores, pesos)

carregado_por_valor = 0
valor_por_valor = 0
for i in range(n):
    item = pesos[i]
    if carregado_por_valor + item <= capacidade:
        carregado_por_valor += item
        valor_por_valor += valores[i]

# Ordenação pela razão de valor por peso
def ordenar_valor(lista, valores, pesos):
    n = len(lista)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lista[j] < lista[j + 1]:
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
                (valores[j], valores[j + 1]) = (valores[j + 1], valores[j])
                (pesos[j], pesos[j + 1]) = (pesos[j + 1], pesos[j])

valor_peso = []
#print(copia_valores, copia_pesos)
for i in range(n):
    valor_peso.append(copia_valores[i] / copia_pesos[i])

ordenar_valor(valor_peso, copia_pesos, copia_valores)

carregado_por_razao = 0
valor_por_razao = 0
for i in range(n):
    item = copia_pesos[i]
    if carregado_por_razao + item <= capacidade:
        carregado_por_razao += item
        valor_por_razao += copia_valores[i]


# Impressão da resposta
print('Valor carregado considerando o peso dos itens: R$', valor_por_peso)
print('Peso carregado considerando o peso dos itens:', carregado_por_peso, 'Kg\n')
print('Valor carregado considerando o valor dos itens: R$', valor_por_valor)
print('Peso carregado considerando o valor dos itens:', carregado_por_valor, 'Kg\n')
print('Valor carregado considerando a razão de valor por peso: R$', valor_por_razao)
print('Peso carregado considerando a razão de valor por peso:', carregado_por_razao, 'Kg')
