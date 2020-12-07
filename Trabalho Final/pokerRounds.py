# Será considerado a "mesa" como o conjunto de cartas dispostas tanto para o jogador quando para o "dealer"
# O "dealer" representa as 5 cartas que podem ser abertas durantes as rodadas
import random
from handsInPoker import verifyHands
from bets import agressive, median, passive

class Player:
    def __init__(self, card1, card2, money, points):
        self.card1 = card1
        self.card2 = card2
        self.money = money
        self.points = points

# Carta possui: valor e naipe da carta e indice de valor
class Card:
    def __init__(self,name,suit,value):
        self.name = name
        self.suit = suit
        self.value = value  
    def __str__(self):
        return (str(self.name) + str(self.suit))
    def __repr__(self):
        return str(self)  
    def get_value(self): 
        return self.__value
    
def fillDeck():
    deck = []
    suits = ['♣', '♦', '♥', '♠'] 
    values = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    for i in range(0,len(values)):
        for j in range(0,len(suits)):
            deck.append(Card(values[i],suits[j],i+2))
    return deck

def dealCards(deck,qtd_p):
    dealer = []
    players = []
    for i in range(0,qtd_p):
        players.append([deck[i],deck[i+qtd_p]])    
    for i in range(qtd_p*2,qtd_p*2+5):
        dealer.append(deck[i])
    del(deck[0:(qtd_p*2+5)]) # retira cartas já distribuídas
    return [deck, players, dealer]

# Soma cartas do jogador para verificar em combinações iguais qual tem maior valor:
def sumCards(comb):
    sum = 0
    for i in range(len(comb)):
        sum += comb[i].value**2  
    return sum

# Montar mão a partir das cartas do flop (river e turn também) + cartas do jogador
def createHand(hand,p):
    comb = []
    for i in range(len(hand)):
        comb.append(hand[i])
    comb.append(p.card1)
    comb.append(p.card2)
    return comb

def main():
    #matches = []
    #countMatches = 0
    #while(countMatches < 100):
    deck = fillDeck()
    random.shuffle(deck)
    table = dealCards(deck,2)
    p = []
    hand = table[2]
    count = 0
    # Distribui a economia inicial para os jogadores
    for i in table[1]:
        p.append(Player(i[0],i[1],1000,0))

    # As apostas seguem até que o primeiro jogador não tenha mais economia
    while (p[0].money > 0 and p[1].money > 0):        
        count += 1
        points = [0,0]
        pot = 0
        bet = [0,0]
        # Disposição das cartas da rodada atual
        #print(mesa[1],mao)  
        # Verifica a mão do jogador, a aposta dele, a pontuação pela combinação e o pote
        for i in range(len(p)):
            if(p[i].money > 0):
                bet[i] =(agressive(p[i],count))
                p[i].money -= bet[i]
                comb = createHand(hand,p[i])
                maxComb = verifyHands(comb)
                p[i].points = maxComb + sumCards(comb)
                points[i] = (p[i].points)
                #print("Jogador " + str(i+1) + ": " + str(p[i].points) + " - Aposta: " + str(bet[i]))
                pot = pot + bet[i]

        #Valor do pote
        #print("Pote: " + str(pote))
        # Anula pontos de jogador que não apostou
        for i in range(len(p)):
            if bet[i] == 0:
                p[i].points = 0
                points[i] = 0
        # Premia jogador com maior pontuação
        for i in range(len(p)):
            if (p[i].points == max(points)) and (min(points) != max(points)) and (bet[i] > 0) and (max(points) > 0):
                p[i].money += pot
            elif (p[i].points == max(points)) and (min(points) == max(points)) and (bet[i] > 0) and (max(points) > 0):
                p[i].money += pot/2  
        # Criação de nova rodada
        deck = fillDeck()
        random.shuffle(deck)
        mesa = dealCards(deck,2)
        mao = mesa[2]
        for j in range(len(mesa[1])):
            p[j].card1 = mesa[1][j][0]
            p[j].card2 = mesa[1][j][1]

    print("Player 1 - Cash: " + str(p[0].money))
    print("Player 2 - Cash: " + str(p[1].money))
    print("Quantidade de Rodadas: ", count)
    print()
        #partidas.append(count)
        #count_partidas += 1

    #soma = 0
    #for i in range(len(partidas)):
     #   soma += partidas[i]
    
    #media = soma/100
    #print(media)

main()