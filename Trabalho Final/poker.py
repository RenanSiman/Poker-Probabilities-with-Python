# Será considerado a "mesa" como o conjunto de cartas dispostas tanto para o jogador quando para o "dealer"
# O "dealer" representa as 5 cartas que podem ser abertas durantes as rodadas

import random
import numpy as np

# Carta possui: valor e naipe da carta e indice de valor
class Carta:
    def __init__(self,carta_v,carta_n,v):
        self.carta_v = carta_v
        self.carta_n = carta_n
        self.v = v
    
    def __str__(self):
        return (str(self.carta_v) + str(self.carta_n))

    def __repr__(self):
        return str(self)
    
def preencher_baralho():
    baralho = []
    naipes = ['♣', '♦', '♥', '♠'] 
    valores = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    for i in range(0,len(valores)):
        for j in range(0,len(naipes)):
            baralho.append(Carta(valores[i],naipes[j],i+2))
    
    return baralho

def distribuir_cartas(baralho):
    dealer = []
    jogadores = []

    for i in range(0,8):
        jogadores.append([baralho[i],baralho[i+8]])    
    for i in range(16,21):
        dealer.append(baralho[i])
    del(baralho[0:21]) # retira cartas já distribuídas

    return [baralho, jogadores, dealer]

# Verificar combinações

def checar_sequencia(mao,jog):
    comb = [mao[0],mao[1],mao[2],jog[0],jog[1]]
    max = comb[0].v
    min = comb[0].v
    aux = []

    # Verifica duplicidade
    for x in range(len(comb)):
        if comb[x].v not in aux:
            aux.append(comb[x].v)
    
    # Verifica maior e menor índices 
    for i in range(1,len(comb)):
        if comb[i].v > max:
            max = comb[i].v
        if comb[i].v < min:
            min = comb[i].v

    print(max,min)

    # Se a diferença entre o maior e menor índices for 4 e todas as cartas são de valores diferentes, então temos sequência
    if (max - min) == 4 and (len(comb) == len(aux)):
        return True
    else:
        return False

def checar_naipe_igual(mao,jog):
    comb = [mao[0],mao[1],mao[2],jog[0],jog[1]]
    aux = []
    
    # Verifica duplicidade
    for x in range(len(comb)):
        if comb[x].carta_n not in aux:
            aux.append(comb[x].carta_n)
    
    if len(comb) == len(aux):
        return True
    else:
        return False

def checar_par(mao,jog):
    return True

def checar_2pares(mao,jog):
    return True

def checar_trinca(mao,jog):
    return True

def checar_quadra(mao,jog):
    return True

    
def prob_jogadores(baralho,jogadores, dealer):
    for i in range(len(dealer)):
        baralho.append(dealer[i])

    return 0

def main():
    baralho = preencher_baralho()
    random.shuffle(baralho)
    mesa = distribuir_cartas(baralho)
    flop = [mesa[2][0],mesa[2][1], mesa[2][2]]
    turn = mesa[2][3]
    river = mesa[2][4]
    print(mesa[1],mesa[2])
    for i in range(len(mesa[1])):
        print("É sequência? ",checar_sequencia(flop,mesa[1][i]))
        naipe_igual = checar_naipe_igual(flop,mesa[1][i])
        print("Naipes Iguais? ",naipe_igual)

main()