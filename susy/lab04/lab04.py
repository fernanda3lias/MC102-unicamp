###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Pedra, Papel e Tesoura 2.0
# Nome: Fernanda Elias
# RA: 259427
###################################################

# Leitura dos valores de força de cada jogador
bonus_jogador_1 = int(input())
bonus_jogador_2 = int(input())
vitorias_jogador_1 = 0
vitorias_jogador_2 = 0
empate = 0

def gerar_resultados(jogada_jogador_1, jogada_jogador_2):
    if jogada_jogador_1 == "Pedra":
      num_jogador_1 = 0
    
    elif jogada_jogador_1 == "Papel":
      num_jogador_1 = 1
    
    elif jogada_jogador_1 == "Tesoura":
      num_jogador_1 = 2


    if jogada_jogador_2 == "Pedra":
      num_jogador_2 = 0
    
    elif jogada_jogador_2 == "Papel":
      num_jogador_2 = 1
    
    elif jogada_jogador_2 == "Tesoura":
      num_jogador_2 = 2

    resultado = (num_jogador_1 - num_jogador_2) % 3

    return resultado


# Processamento dos dados
#...
while True:
  entrada = input().split()
  if entrada[0] == '0':
    break
  else:
    jogada_jogador_1, forca_jogador_1, jogada_jogador_2, forca_jogador_2, fator_rodada = entrada
    forca_jogador_1 = int(forca_jogador_1)
    forca_jogador_2 = int(forca_jogador_2)
    fator_rodada = int(fator_rodada)

    resultado = gerar_resultados(jogada_jogador_1=jogada_jogador_1, jogada_jogador_2=jogada_jogador_2)


    # Calculando forças
    if forca_jogador_1 != 1:
      if (forca_jogador_1 - 1) < bonus_jogador_1:
        bonus_jogador_1 -= (forca_jogador_1 - 1)
        forca_jogador_1 =  forca_jogador_1

      else:
        forca_jogador_1 =  bonus_jogador_1 + 1
        bonus_jogador_1 = 0
    else:
      forca_jogador_1 = 1

    if forca_jogador_2 != 1:
      if (forca_jogador_2 - 1) < bonus_jogador_2:
        bonus_jogador_2 -= (forca_jogador_2 - 1)
        forca_jogador_2 =  forca_jogador_2

      else:
        forca_jogador_2 =  bonus_jogador_2 + 1
        bonus_jogador_2 = 0
    
    else:
      forca_jogador_2 = 1

    #print("forcas", forca_jogador_1, forca_jogador_2)
    #print("bonus", bonus_jogador_1, bonus_jogador_2)
      
      #Jogada com bônus
      ###
    if jogada_jogador_1 != jogada_jogador_2:
      if resultado == 1:
        forca_jogador_2 *= fator_rodada

        if forca_jogador_2 > forca_jogador_1:
          vitorias_jogador_2 += 1

        elif forca_jogador_1 > forca_jogador_2:
          vitorias_jogador_1 +=1

        else:
          vitorias_jogador_1 +=1

      if resultado == 2:
        forca_jogador_1 *= fator_rodada

        if forca_jogador_1 > forca_jogador_2:
          vitorias_jogador_1 += 1

        elif forca_jogador_2 > forca_jogador_1:
          vitorias_jogador_2 += 1

        else:
          vitorias_jogador_2 +=1

    else:
      if forca_jogador_2 > forca_jogador_1:
        vitorias_jogador_2 += 1
      
      elif forca_jogador_1 > forca_jogador_2:
        vitorias_jogador_1 +=1

      else:
        empate += 1

    #print("vitorias", vitorias_jogador_1, vitorias_jogador_2, empate)


# Saída de dados
print('Vitórias do jogador 1:', vitorias_jogador_1)
print('Vitórias do jogador 2:', vitorias_jogador_2)
print('Empates:', empate)
