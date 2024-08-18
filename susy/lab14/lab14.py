    ###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Montanha Russa II
# Nome: Fernanda
###################################################
"""
Função para simular a compra de ações, que deve ser implementada de forma recursiva.

Argumentos:
    - precos: a matriz contendo o preço diário das ações de cada uma das empresas
    - dia (int): o dia corrente
    - dinheiro (int): o capital inicial a sua disposição no dia especifico
    - acoes_compradas (int): a quantidade de ações em sua posse no dia atual
    - empresa_comprada (int): o índice representando a empresa cujas ações compradas estão em sua posse

IMPORTANTE: A submissão de um programa sem uma FUNÇÃO RECURSIVA válida
            implementada será considerada TENTATIVA DE FRAUDE.
"""
def simula_compra_acoes(precos, dia, dinheiro, acoes_compradas, empresa_comprada):

    print(dia)
    if dia == len(precos):
        print("finalizando")
        return 

    elif dia == len(precos)-1:
        return 
    
    else:
        for n in range(len(precos[0])):
            D1 = precos[dia][n]
            D2 = precos[dia+1][n]

            if D1 < D2:
                x = int(dinheiro // D1)
                #print(x)
                lucro = D2 * x
                resto = dinheiro % D1
                #print(resto)
                lucro = lucro + resto

                print("lucro da empresa", n, "é", lucro)

            else:
                ...


    aux = simula_compra_acoes(precos, dia+1, dinheiro, acoes_compradas, empresa_comprada)


# Leitura de dados
N, M = map(int, input().split())
precos = []

for i in range(N):
    precos.append(list(map(int, input().split())))

dinheiro = int(input())

# Cálculo dos dias de compra e venda
acoes_compradas = 0
empresa_comprada = 0
dia = 0

aux = simula_compra_acoes(precos, dia, dinheiro, acoes_compradas, empresa_comprada)

# Impressão da saída
if __name__ == "__main__":
    ...