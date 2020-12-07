# Verify hands
from itertools import combinations

def checkPair(comb):
    aux = []
    for i in range(len(comb)):
        aux.append(comb[i].value)   
    pair = []
    for i in aux:
        pair.append(aux.count(i)) 
    if (pair.count(2) == 2):
        return True
    else:
        return False

def check2Pairs(comb):
    aux = []
    for i in range(len(comb)):
        aux.append(comb[i].value)   
    pairs = []
    for i in aux:
        pairs.append(aux.count(i)) 
    if pairs.count(2) == 4:
        return True
    else:
        return False

def checkThreeOfAKind(comb):
    aux = []
    for i in range(len(comb)):
        aux.append(comb[i].value)  
    triplet = []
    for i in aux:
        triplet.append(aux.count(i)) 
    if (triplet.count(3) == 3):
        return True
    else:
        return False

def checkStraight(comb):
    max = comb[0].value
    min = comb[0].value
    aux = []
    # Verifica duplicidade
    for x in range(len(comb)):
        if comb[x].value not in aux:
            aux.append(comb[x].value)    
    # Verifica maior e menor índices 
    for i in range(1,len(comb)):
        if comb[i].value > max:
            max = comb[i].value
        if comb[i].value < min:
            min = comb[i].value
    # Se a diferença entre o maior e menor índices for 4 e todas as cartas são de valores diferentes, então temos sequência
    if (max - min) == 4 and (len(comb) == len(aux)):
        return True
    else:
        return False

def checkFlush(comb):
    aux = [] 
    # Verifica duplicidade
    for x in range(len(comb)):
        aux.append(comb[x].suit)
    flush = []
    for i in aux:
        flush.append(aux.count(i)) 
    if (flush.count(5) == 5):
        return True
    else:
        return False

def checkFullHouse(comb):
    if (checkPair(comb) == True) and (checkThreeOfAKind(comb) == True):
        return True
    else:
        return False

def checkFourOfAKind(comb):
    aux = []
    for i in range(len(comb)):
        aux.append(comb[i].value) 
    fourfold = []
    for i in aux:
        fourfold.append(aux.count(i)) 
    if fourfold.count(4) == 4:
        return True
    else:
       return False

def checkStraightFlush(comb):
    v = []
    for i in range(len(comb)):
        v.append(comb[i].value)
    if (checkStraight(comb) == True) and (checkFlush(comb) == True) and (max(v) < 14):
        return True
    else:
        return False
    
def checar_royal_flush(comb):
    max = comb[0].value
    # Verifica maior índice
    for i in range(1,len(comb)):
        if comb[i].value > max:
            max = comb[i].value
    if (checkStraightFlush(comb) == True) and (max == 14):
        return True
    else:
        return False

# Define a pontuação conforme a combinação do Jogador. Será usada para determinar se o jogador venceu ou não a rodada
def verifyComb(comb):
    if checar_royal_flush(comb) == True:
        return 100000
    elif checkStraightFlush(comb) == True:
        return 90000
    elif checkFourOfAKind(comb) == True:
        return 80000
    elif checkFullHouse(comb) == True:
        return 70000
    elif checkFlush(comb) == True:
        return 60000
    elif checkStraight(comb) == True:
        return 50000
    elif (checkThreeOfAKind(comb) == True) and (checkPair(comb) == False):
        return 40000
    elif check2Pairs(comb) == True:
        return 30000
    elif (checkPair(comb) == True) and (checkThreeOfAKind(comb) == False):
        return 20000
    else:
        return 10000

# Melhor combinação em turn
def verifyHands(comb):
    suits = []
    values = []
    for i in range(len(comb)):
        suits.append(comb[i].suit)
        values.append(comb[i].value)
    resVerifying = []
    for subcomb in combinations(comb,5):
        resVerifying.append(verifyComb(subcomb))  
    return max(resVerifying)