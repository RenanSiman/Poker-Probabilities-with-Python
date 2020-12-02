# Será considerado a "mesa" como o conjunto de cartas dispostas tanto para o jogador quando para o "dealer"
# O "dealer" representa as 5 cartas que podem ser abertas durantes as rodadas

import random
import csv
import numpy as np

class Jogador:
    def __init__(self, carta_1, carta_2, dinheiro, pontos):
        self.carta_1 = carta_1
        self.carta_2 = carta_2
        self.dinheiro = dinheiro
        self.pontos = pontos

# Carta possui: valor e naipe da carta e indice de valor
class Carta:
    def __init__(self,nome,naipe,valor):
        self.nome = nome
        self.naipe = naipe
        self.valor = valor
    
    def __str__(self):
        return (str(self.nome) + str(self.naipe))

    def __repr__(self):
        return str(self)
    
    def get_valor(self): 
        return self.__valor
    
def preencher_baralho():
    baralho = []
    naipes = ['♣', '♦', '♥', '♠'] 
    valores = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    for i in range(0,len(valores)):
        for j in range(0,len(naipes)):
            baralho.append(Carta(valores[i],naipes[j],i+2))
    
    return baralho

def distribuir_cartas(baralho,qtd_jog):
    dealer = []
    jogadores = []

    for i in range(0,qtd_jog):
        jogadores.append([baralho[i],baralho[i+qtd_jog]])    
    for i in range(qtd_jog*2,qtd_jog*2+5):
        dealer.append(baralho[i])
    del(baralho[0:(qtd_jog*2+5)]) # retira cartas já distribuídas

    return [baralho, jogadores, dealer]

# Soma cartas do jogador para verificar em combinações iguais qual tem maior valor:
def soma_cartas(comb):
    soma = 0
    for i in range(len(comb)):
        soma += comb[i].valor**2
    
    return soma

# Verifica combinações
def checar_par(comb):
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    par = []
    #print(aux)
    for i in aux:
        par.append(aux.count(i)) 

    if (par.count(2) == 2):
        return True
    else:
        return False

def checar_2pares(comb):
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

def checar_trinca(comb):
    aux = []

    for i in range(len(comb)):
        aux.append(comb[i].valor)
    
    trinca = []
    for i in aux:
        trinca.append(aux.count(i)) 

    if (trinca.count(3) == 3):
        return True
    else:
        return False

def checar_straight(comb):
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

def checar_flush(comb):
    aux = []
    
    # Verifica duplicidade
    for x in range(len(comb)):
        aux.append(comb[x].naipe)
    flush = []
    for i in aux:
        flush.append(aux.count(i)) 

    if (flush.count(5) == 5):
        return True
    else:
        return False

def checar_fullhouse(comb):
    if (checar_par(comb) == True) and (checar_trinca(comb) == True):
        return True
    else:
        return False

def checar_quadra(comb):
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

def checar_straight_flush(comb):
    v = []
    for i in range(len(comb)):
        v.append(comb[i].valor)

    if (checar_straight(comb) == True) and (checar_flush(comb) == True) and (max(v) < 14):
        return True
    else:
        return False
    
def checar_royal_flush(comb):
    max = comb[0].valor

    # Verifica maior índice
    for i in range(1,len(comb)):
        if comb[i].valor > max:
            max = comb[i].valor

    if (checar_straight_flush(comb) == True) and (max == 14):
        return True
    else:
        return False

# Montar mão a partir das cartas do flop (river e turn também) + cartas do jogador
def montar_mao(mao,jog):
    comb = []
    for i in range(len(mao)):
        comb.append(mao[i])
    comb.append(jog.carta_1)
    comb.append(jog.carta_2)

    return comb

# Define a pontuação conforme a combinação do Jogador. Será usada para determinar se o jogador venceu ou não a rodada
def verifica_combinacoes(comb):
    if checar_royal_flush(comb) == True:
        return 100000
    elif checar_straight_flush(comb) == True:
        return 90000
    elif checar_quadra(comb) == True:
        return 80000
    elif checar_fullhouse(comb) == True:
        return 70000
    elif checar_flush(comb) == True:
        return 60000
    elif checar_straight(comb) == True:
        return 50000
    elif (checar_trinca(comb) == True) and (checar_par(comb) == False):
        return 40000
    elif checar_2pares(comb) == True:
        return 30000
    elif (checar_par(comb) == True) and (checar_trinca(comb) == False):
        return 20000
    else:
        return 10000

def apostas(jog,count):
    # importa tabela de mãos iniciais para uma lista
    with open('initial-hands.csv', newline='') as f:
        reader = csv.reader(f)
        datas = list(reader)

    count = count/10 # Aumenta as apostas a cada 10 rodadas

    if jog.dinheiro > 0:
        for data in datas:
            # Verifica na tabela de mãos iniciais qual é a mão do jogador e se ele irá apostar ou não
            if (str(jog.carta_1.nome) == data[0]) and (str(jog.carta_2.nome) == data[1]) or (str(jog.carta_1.nome) == data[1]) and (str(jog.carta_2.nome) == data[0]):
                if (data[2] == "blue") or (data[2] == "green") or (data[2] == "yellow"):
                    return 100*int(count)
                elif (data[2] == "red"):
                    return 0
    else:
        return 0

def main():
    baralho = preencher_baralho()
    random.shuffle(baralho)
    mesa = distribuir_cartas(baralho,2) # para alterar o número de jogadores basta trocar o valor do 2º parâmetro
    flop = [mesa[2][0],mesa[2][1], mesa[2][2]] #, mao = mesa[2]
    jog = []

    # Distribui a economia inicial para os jogadores
    for i in mesa[1]:
        jog.append(Jogador(i[0],i[1],1000,0))
    count = 0
    # As apostas seguem até que o primeiro jogador não tenha mais economia
    while (jog[0].dinheiro > 0 or jog[1].dinheiro > 0):        
        count += 1
        print("Jogador 1 - Economia: " + str(jog[0].dinheiro))
        print("Jogador 2 - Economia: " + str(jog[1].dinheiro))
        print()
        pontos = []
        pote = 0
        aposta = []

        # Disposição das cartas da rodada atual
        print(mesa[1],flop)
        
        # Verifica a mão do jogador, a aposta dele, a pontuação pela combinação e o pote
        for i in range(len(jog)):
            if(jog[i].dinheiro > 0):
                aposta.append(apostas(jog[i],count))
                jog[i].dinheiro -= aposta[i]
                comb = montar_mao(flop,jog[i])
                jog[i].pontos = verifica_combinacoes(comb) + soma_cartas(comb)
                pontos.append(jog[i].pontos)
                print("Jogador " + str(i+1) + ": " + str(jog[i].pontos) + " - Aposta: " + str(aposta[i]))
                pote = pote + aposta[i]

        #Valor do pote
        print("Pote: " + str(pote))

        # Anula pontos de jogador que não apostou
        for i in range(len(jog)):
            if aposta[i] == 0:
                jog[i].pontos = 0
                pontos[i] = 0

        # Premia jogador com maior pontuação
        for i in range(len(jog)):
            if (jog[i].pontos == max(pontos)) and (min(pontos) != max(pontos)) and (aposta[i] > 0) and (max(pontos) > 0):
                jog[i].dinheiro += pote
            elif (jog[i].pontos == max(pontos)) and (min(pontos) == max(pontos)) and (aposta[i] > 0) and (max(pontos) > 0):
                jog[i].dinheiro += pote/2
        
        # Criação de nova rodada
        baralho = preencher_baralho()
        random.shuffle(baralho)
        mesa = distribuir_cartas(baralho,2)
        flop = [mesa[2][0],mesa[2][1], mesa[2][2]]
        for j in range(len(mesa[1])):
            jog[j].carta_1 = mesa[1][j][0]
            jog[j].carta_2 = mesa[1][j][1]

        print("Fim da Rodada: ", count)

main()