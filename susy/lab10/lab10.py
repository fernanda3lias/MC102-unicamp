###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Quadrados à Obra
# Nome: Fernanda
###################################################
def verificar(matriz, M, N):
   aux = [[0] * N for i in range(M)]

   maior_lado, maior_linha, maior_coluna = 0, 0, 0
   for i in range(M):
        # print(i)
        for j in range(N):
            # print(j)
            # print(matriz[i][j])
            if matriz[i][j] == ' ':
                aux[i][j] = min(aux[i-1][j], aux[i][j-1], aux[i-1][j-1]) + 1
                
                if aux[i][j] > maior_lado:
                    maior_lado = aux[i][j]
                    maior_linha = i
                    maior_coluna = j

   return maior_lado, maior_linha, maior_coluna

def desenhar(matriz, maior_linha, maior_coluna, maior_lado):
    for i in range(maior_linha - maior_lado + 1, maior_linha + 1):
        for j in range(maior_coluna - maior_lado + 1, maior_coluna + 1):
            if i == maior_linha - maior_lado + 1 or i == maior_linha or j == maior_coluna - maior_lado + 1 or j == maior_coluna:
                matriz[i][j] = '*'

def main():
    # Leitura do número de setores verticais e horizontais.
    M, N = map(int, input().split())

    terreno = []

    # Leitura do mapa do terreno do cliente.
    for i in range(M):
        linha_i = list(input())
        terreno += [linha_i]

    maior_lado, maior_linha, maior_coluna = verificar(terreno, M, N)

    # print(maior_lado, maior_linha, maior_coluna)

    desenhar(terreno, maior_linha, maior_coluna, maior_lado)

    # print(terreno)

    linha = ""

    for i in range(M):
        for j in range(N): 
            linha += terreno[i][j]
        
        print(linha)
        linha = ""


if __name__ == "__main__":
  main()