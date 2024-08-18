###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Pac-Man I
# Nome: Fernanda
###################################################

# Leitura da entrada
N = int(input())
T = int(input())

mapa = []
for _ in range(N):
    mapa.append(list(input()))

def printar_matriz(matriz):
    for i in matriz:
        linha = ""
        for j in i:
            linha += str(j)
        print(linha)

# Simulação do jogo
def achar_pac(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "C":
                return i, j

def count_food(mapa):
    total_food = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "." or mapa[i][j] == "*":
                total_food += 1
    return total_food

def game(mapa, localizacao, comidas, direcao, power, tempo_restante, i):
    y, x = localizacao
    linhas = len(mapa)
    colunas = len(mapa[0])

    # direita, baixo, esqueda, cima
    direcoes = {'d': (0, 1), 'b': (1, 0), 'e': (0, -1), 'c': (-1, 0)}

    ordem = {
        'd': ['b', 'd', 'c', 'e'],
        'b': ['e', 'b', 'd', 'c'],
        'e': ['c', 'e', 'b', 'd'],
        'c': ['d', 'c', 'e', 'b']
    }

    movido = False

    for dir in ordem[direcao]:
        dy, dx = direcoes[dir]
        novo_y = (y + dy) % linhas
        novo_x = (x + dx) % colunas
        if mapa[novo_y][novo_x] != "#":
            if mapa[novo_y][novo_x] == "*":
                power = True
                comidas += 1
                tempo_restante = T
            elif mapa[novo_y][novo_x] == "X":
                if not power:
                    return None, comidas, direcao, power, i
            elif mapa[novo_y][novo_x] == ".":
                comidas += 1
            
            mapa[novo_y][novo_x] = "C"
            mapa[y][x] = " "
            localizacao = (novo_y, novo_x)
            direcao = dir
            movido = True
            break

    if not movido:
        for dir in ordem[direcao]:
            dy, dx = direcoes[dir]
            novo_y = (y + dy) % linhas
            novo_x = (x + dx) % colunas
            if mapa[novo_y][novo_x] != "#":
                localizacao = (novo_y, novo_x)
                direcao = dir
                break

    if power:
        if i < tempo_restante:
            i += 1
        else:
            power = False
            i = 0

    #printar_matriz(mapa)
    
    return localizacao, comidas, direcao, power, i

# Impressão da saída
if __name__ == "__main__":
    localizacao = achar_pac(mapa)
    comidas = 0
    direcao = "d"
    power = False
    i = 0

    total_food = count_food(mapa)

    while True:
        localizacao, comidas, direcao, power, i = game(mapa, localizacao, comidas, direcao, power, T, i)

        if localizacao is None or total_food == comidas:
            print(comidas)
            break

        #print(localizacao)
        #print(comidas)
