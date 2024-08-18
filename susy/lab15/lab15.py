###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Pac-Man II
# Nome: Fernanda
###################################################
'''
Função para simular um caminho percorrido pelo Pac-Man, essa função deve ser
implementada de forma recursiva. A função recebe a matriz representando o
mapa, a posição (i,j) do pacman, uma variável dir representando a direção
atual, o tempo t de duração do pastilha de poder ativa (se houver), o valor
T e o número de pastilhas recolhidas até o momento. A função deve retornar o
número de pastilhas comidas pelo Pac-Man.

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
'''

def simula_caminho(mapa, i, j, dir, t, T, pastilhas, caminho, melhor_caminho, max_pastilhas, visitados):
    if mapa[i][j] == 'X' and t == 0: 
        return pastilhas, caminho

    pastilhas_inicial = pastilhas 
    if mapa[i][j] == '.':
        pastilhas += 1
        mapa[i][j] = ' ' 
    elif mapa[i][j] == '*':
        pastilhas += 1
        t = T + 1  
        mapa[i][j] = ' ' 

    if pastilhas > max_pastilhas[0]:
        max_pastilhas[0] = pastilhas
        melhor_caminho[:] = caminho[:]

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for d in direcoes:
        ni, nj = i + d[0], j + d[1]

        ni = (ni + N) % N
        nj = (nj + len(mapa[0])) % len(mapa[0])

        if mapa[ni][nj] != '#' and d != (-dir[0], -dir[1]):
            novo_caminho = caminho + [(ni, nj)]

            estado_atual = (ni, nj, d, t)
            if estado_atual in visitados:
                continue  
            visitados.add(estado_atual)

            simula_caminho(mapa, ni, nj, d, max(0, t - 1), T, pastilhas, novo_caminho, melhor_caminho, max_pastilhas, visitados)

            visitados.remove(estado_atual)

    if pastilhas > pastilhas_inicial:
        if t == T + 1:
            mapa[i][j] = '*' 
        else:
            mapa[i][j] = '.'  

    return max_pastilhas[0], melhor_caminho

# Leitura da entrada
N = int(input())
T = int(input())

mapa = []
for _ in range(N):
    mapa.append(list(input()))

for i in range(N):
    for j in range(len(mapa[i])):
        if mapa[i][j] == 'C':
            start_i, start_j = i, j
            mapa[i][j] = ' ' 

# Simulação do jogo
max_pastilhas = [0]
melhor_caminho = []
visitados = set()
result, caminho = simula_caminho(mapa, start_i, start_j, (0, 0), 0, T, 0, [(start_i, start_j)], melhor_caminho, max_pastilhas, visitados)

# Impressão da saída
print(result)
