###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 08 - Calculadora genômica
# Nome: Fernanda
###################################################


# Definindo comandos
def reverter(cadeia:str, i:int, j:int):
    _cadeia = ""

    if i > j:
        sub = cadeia[i:] + cadeia[:j+1]
        middle = cadeia.replace(cadeia[i:], "")
        middle = middle.replace(cadeia[:j+1], "")

        sub = sub[::-1]
        _cadeia = sub[len(cadeia)-i:] + middle + sub[:len(cadeia)-i]
    
    else:
        _cadeia = cadeia[i:j+1]
        _cadeia = _cadeia[::-1]
        _cadeia = cadeia[:i] + _cadeia + cadeia[j+1:]

    return _cadeia


def transpor(cadeia:str, i:int, j:int, k:int):
    sub1, sub2 = cadeia[i:j+1], cadeia[j+1:k+1]
    _cadeia = cadeia[:i] + sub2 + sub1 + cadeia[k+1:]

    return _cadeia

def inserir(cadeia:str, g:str, i:int):
    _cadeia = cadeia[:i] + g + cadeia[i:]

    return _cadeia

def remover(cadeia:str, i:int, j:int):
    _cadeia = cadeia[:i] + cadeia[j+1:]

    return _cadeia

def fissao(cadeia:str, i:int):

    _cadeia = ""
    m = 0
    for k in range(len(cadeia)):
        if k == i:
            for l in range(len(cadeia)):
                if k >= len(cadeia):

                    _cadeia += cadeia[m]
                    m += 1
                
                else:
                    _cadeia += cadeia[k]
                    k += 1
    return _cadeia



def fusao(cadeia:str):
    # Transforma genoma linear em ciclico
    _sufixo = "c1"

    return _sufixo

def mostrar(cadeia:str, sufixo:str):
    # Mostra a cadeia
    print(cadeia, sufixo)

def buscar(cadeia:str, g:str, sufixo:str):
    if sufixo == "c0":
        _counter = cadeia.count(g)
    
    else:
        cadeia = cadeia + cadeia[:len(g)]
        _counter = cadeia.count(g)
    
    return _counter


# 
cadeia = input()
sufixo = "c0"

if "c1" in cadeia:
    cadeia, sufixo = cadeia.split(" ")

sair = False

while sair == False:
    comando = input()

    if "reverter" in comando:
        comando, i, j = comando.split(" ")
        i = int(i)
        j = int(j)

        cadeia = reverter(cadeia, i, j)
    
    elif "mostrar" in comando:
        mostrar(cadeia, sufixo)

    elif "inserir" in comando:
        comando, g, i = comando.split()
        i = int(i)
        cadeia = inserir(cadeia, g, i)

    elif "remover" in comando:
        comando, j, i = comando.split()
        j = int(j)
        i = int(i)
        cadeia = remover(cadeia, j, i)

    elif "fusao" in comando:
        sufixo = fusao(cadeia)

    elif "buscar" in comando:
        comando, g = comando.split(" ")
        counter = buscar(cadeia, g, sufixo)

        print(counter)

    elif "fissao" in comando:
        comando, i = comando.split(" ")
        i = int(i)
        cadeia = fissao(cadeia, i)
        sufixo = "c0"
    
    elif "transpor" in comando:
        comando, i, j, k = comando.split(" ")
        i = int(i)
        j = int(j)
        k = int(k)

        cadeia = transpor(cadeia, i, j, k)

    elif comando == "sair":
        sair = True

