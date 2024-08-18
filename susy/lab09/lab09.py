###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Anonimizador de Texto
# Nome: Fernanda
###################################################
import re

# Definição de funções
def extrair_nome(frase, lista):
    padrao_nome = r'(?:\s[A-Z]\w*){2,}'
    nomes = re.findall(padrao_nome, frase)

    if nomes:
        for i in nomes:
            lista.append(i)

    return lista


def extrair_cpf(frase, lista):
    padrao_cpf = r'((?:[0-9]{3}\.){2}(?:[0-9]){3}-(?:[0-9]){2})|((?:[0-9]{9})-(?:[0-9]{2}))'
    cpf = re.findall(padrao_cpf, frase)

    #print(cpf)

    if cpf:
        for i in cpf:
            if len(i) > 1:
                for j in i:
                    if j != '':
                        lista.append(j)
            
            else:
                if i != '':
                    lista.append(i)

    return lista

def extrair_cartao(frase, lista):
    padrao_cartao = r'\d{4}\s\d{4}\s\d{4}\s\d{4}'
    cartao = re.findall(padrao_cartao, frase)

    if cartao:
        for i in cartao:
            lista.append(i)

    padrao_cartao = r'\d{16}'
    cartao = re.findall(padrao_cartao, frase)

    if cartao:
        for i in cartao:
            lista.append(i)

    #print(lista)

    return lista

def extrair_data(frase, lista):
    padrao_data = r'(?:\d{2})/(?:\d{2})/(?:\d{4})'
    data = re.findall(padrao_data, frase)

    if data:
        for i in data:
            lista.append(i)

    return lista

def extrair_email(frase, lista):
    padrao_email = r'\b(?:[A-Za-z0-9._%+-])+@(?:[A-Za-z0-9.-])+\.(?:[A-Z|a-z]){2,}\b'
    email = re.findall(padrao_email, frase)

    if email:
        for i in email:
            lista.append(i)

    return lista


# Anonimização do texto
def anonimizador(frase, lista):

    lista = extrair_nome(frase, lista)
    lista = extrair_cpf(frase, lista)
    lista = extrair_cartao(frase, lista)
    lista = extrair_data(frase, lista)
    lista = extrair_email(frase, lista)

    return lista

def construtor(frase, lista, antiga_lista):
    global counter
    global cc
    gg = 0
    lista_sorted = sorted(lista, key=lambda x: frase.index(x))

    for i in lista_sorted:
        
        if i not in lista_geral:
            search_nome = re.search(r'(?:\s[A-Z]\w*){2,}', i)
            search_cpf = re.search(r'((?:[0-9]{3}\.){2}(?:[0-9]){3}-(?:[0-9]){2})|(?:[0-9]{3}){2}[0-9]{3}-[0-9]{2}', i)
            search_cartao = re.search(r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b', i)
            search_data =  re.search(r'(?:\d{2})/(?:\d{2})/(?:\d{4})', i)
            search_email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', i)

            if search_nome:
                if i ==  search_nome.group():
                    counter += 1
                    lista_ids.append(f" nome:{counter}")
                    lista_geral.append(i)
                   

            if search_cpf:
                if i ==  search_cpf.group():
                    for k in lista:
                        if i  and k:
                            if i!=k and i == k.replace(".",""):
                                gg = 1
                                #print(i , k)
                    
                    if gg == 0:
                        counter += 1
                        lista_ids.append(f"cpf:{counter}")
                        lista_geral.append(i)


            if search_cartao:
                if cc == False:
                    counter += 1
                    if i ==  search_cartao.group():
                        lista_ids.append(f"cartao:{counter}")
                        lista_geral.append(i)

                        cc = True
            if cc == False:
                search_cartao = re.search(r'\d{16}', i)
                if search_cartao:
                    if i ==  search_cartao.group():
                        counter += 1
                        lista_ids.append(f"cartao:{counter}")
                        lista_geral.append(i)
                        cc = True

            if search_data:
                if i ==  search_data.group():
                    counter += 1
                    lista_ids.append(f"data:{counter}")
                    lista_geral.append(i)


            if search_email:
                if i ==  search_email.group():
                    counter += 1
                    lista_ids.append(f"email:{counter}")
                    lista_geral.append(i)

    nova_frase = frase

    #print(lista_ids, lista_geral)

    for j in range(len(lista_geral)):
        if "cartao" in lista_ids[j]:
            nova_frase = re.sub(lista_geral[j].replace(" ",""), lista_ids[j], nova_frase)

        if "cpf" in lista_ids[j]:
            nova_frase = re.sub(lista_geral[j].replace(".",""), lista_ids[j], nova_frase)

        nova_frase = re.sub(lista_geral[j], lista_ids[j], nova_frase)

    print(nova_frase)

    return 0

# Definição de variáveis globais
lista_anterior = []
lista_geral    = [] 
lista_ids      = []     
counter = 0
cc = False

# Impressão da saída
while True:
    lista = []
    frase = input()

    if frase == "-":
        break

    lista = anonimizador(frase, lista)
    nova_frase = construtor(frase, lista, lista_anterior)

    lista_anterior = lista

    #print(lista_geral)
    #print(lista_ids)


