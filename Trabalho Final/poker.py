# Será considerado a "mesa" como o conjunto de cartas dispostas tanto para o jogador quando para o "dealer"
# O "dealer" representa as 5 cartas que podem ser abertas durantes as rodadas

import random
import csv
import numpy as np

# Carta possui: valor e naipe da carta e indice de valor
class Carta:
    def __init__(self,nome,naipe,v):
        self.nome = nome
        self.naipe = naipe
        self.valor = v
    
    def __str__(self):
        return (str(self.nome) + str(self.naipe))

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

# Soma cartas do jogador para verificar em combinações iguais qual tem maior valor:
def soma_cartas(mao,jog):
    soma = 0
    for i in range(len(mao)):
        soma += mao[i].valor
    
    for i in range(len(jog)):
        soma += jog[i].valor
    
    return soma

# Verificar combinações

def checar_par(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    par = []
    #print(aux)
    for i in aux:
        par.append(aux.count(i)) 

    if (par.count(2) == 2) and (checar_trinca(mao,jog) == False):
        return True
    else:
       return False

def checar_2pares(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    pares = []
    for i in aux:
        pares.append(aux.count(i)) 

    if pares.count(2) == 4:
        return True
    else:
       return False

def checar_trinca(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    trinca = []
    for i in aux:
        trinca.append(aux.count(i)) 

    if (trinca.count(3) == 3) and (checar_par(mao,jog) == False):
        return True
    else:
       return False

def checar_straight(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    max = comb[0].valor
    min = comb[0].valor
    aux = []

    # Verifica duplicidade
    for x in range(len(comb)):
        if comb[x].valor not in aux:
            aux.append(comb[x].valor)
    
    # Verifica maior e menor índices 
    for i in range(1,len(comb)):
        if comb[i].valor > max:
            max = comb[i].valor
        if comb[i].valor < min:
            min = comb[i].valor

    #print(max,min)

    # Se a diferença entre o maior e menor índices for 4 e todas as cartas são de valores diferentes, então temos sequência
    if (max - min) == 4 and (len(comb) == len(aux)):
        return True
    else:
        return False

def checar_flush(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    aux = []
    
    # Verifica duplicidade
    for x in range(len(comb)):
        if comb[x].naipe not in aux:
            aux.append(comb[x].naipe)
    
    if len(comb) == len(aux):
        return True
    else:
        return False

def checar_fullhouse(mao,jog):
    if (checar_par == True) and (checar_trinca == True):
        return True
    else:
        return False

def checar_quadra(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    for i in range(len(jog)):
        comb.append(jog[i])
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    quadra = []
    for i in aux:
        quadra.append(aux.count(i)) 

    if quadra.count(4) == 4:
        return True
    else:
       return False

def checar_straight_flush(mao,jog):
    if (checar_straight(mao,jog) == True) and (checar_flush(mao,jog) == True):
        return True
    else:
        return False
    
def checar_royal_flush(mao,jog):
    comb = [mao[0],mao[1],mao[2],jog[0],jog[1]]
    max = comb[0].valor

    # Verifica maior índice
    for i in range(1,len(comb)):
        if comb[i].valor > max:
            max = comb[i].valor

    if (checar_straight(mao,jog) == True) and (checar_flush(mao,jog) == True) and (max == 14):
        return True
    else:
        return False

def verifica_combinacoes(mao,jog):
    if checar_par(mao, jog) == True:
        return 200
    elif checar_2pares(mao, jog) == True:
        return 300
    elif checar_trinca(mao, jog) == True:
        return 400
    elif checar_straight(mao, jog) == True:
        return 500
    elif checar_flush(mao, jog) == True:
        return 600
    elif checar_fullhouse(mao, jog) == True:
        return 700
    elif checar_quadra(mao, jog) == True:
        return 800
    elif checar_straight_flush(mao, jog) == True:
        return 900
    elif checar_royal_flush(mao, jog) == True:
        return 1000
    else:
        return 100
def main():
    baralho = preencher_baralho()
    random.shuffle(baralho)
    mesa = distribuir_cartas(baralho)
    flop = [mesa[2][0],mesa[2][1], mesa[2][2]]
    turn = mesa[2][3]
    river = mesa[2][4]
    print(mesa[1],mesa[2])
    for i in range(len(mesa[1])):
        print("Jogador " + mesa[1][i].__str__() + " - " + str(verifica_combinacoes(flop,mesa[1][i]) + soma_cartas(flop, mesa[1][i])))
        
main()