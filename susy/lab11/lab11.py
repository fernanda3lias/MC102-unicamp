###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Níveis de Radiação
# Nome: Fernanda
###################################################
import numpy as np

def create_matriz(M, N, location, original, lista):
    p, q = location[0], location[1]
    valor = int(original[p][q])
    matrizes = []

    zerada = np.zeros((M, N), dtype=int)
    matriz = np.array(zerada)

    matriz[p][q] = valor

    for i in range(1, valor):
        new_value = valor - i
        for x in range(-i, i+1):
            for y in range(-i, i+1):
                if 0 <= p + x < M and 0 <= q + y < N:
                    if abs(x) == i or abs(y) == i:
                        matriz[p + x][q + y] = new_value
        copia = matriz.copy().tolist()
        matrizes.append(copia)

    zerada = zerada.tolist()

    for i in range(M):
        for j in range(N):
            for ma in matrizes:
                if zerada[i][j] == 0:
                    zerada[i][j] = ma[i][j]

    zerada[p][q] = valor
    lista.append(zerada.copy())



def printar_matriz(matriz):
    for i in matriz:
      linha = ""
      for j in i:
         linha += str(j)
      
      print(linha)

def somar_matrizes(matrizes, M, N):
   soma = np.zeros((M, N), dtype=int)

   for matriz in matrizes:
    soma += np.array(matriz)

   soma = np.where(soma > 9, '+', soma)

   return soma.tolist()

matrizes = []
area = []
# Leitura de dados
linhas = int(input())
for i in range(linhas):
  linha_i = list(input())
  area += [linha_i]

# Processamento
elements = []
for i in range(len(area)):
  for j in range(len(area[i])):
    value = area[i][j]
    if value != "0":
      elements.append((i, j))

for i in elements:
   matriz = create_matriz(linhas, len(area[0]), i, area, matrizes)

#print(matrizes)  
soma = somar_matrizes(matrizes, linhas, len(area[0]))

printar_matriz(soma)

# Impressão da saída
'''
for linha in niveis:
  print(''.join(linha))
'''