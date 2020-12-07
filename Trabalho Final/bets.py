import csv

def agressive(p,count):
    # importa tabela de mãos iniciais para uma lista
    with open('initial-hands.csv', newline='') as f:
        reader = csv.reader(f)
        datas = list(reader)
    count = count/10 + 1 # Aumenta as apostas a cada 10 rodadas
    if p.money > 0:
        for data in datas:
            # Verifica na tabela de mãos iniciais qual é a mão do jogador e se ele irá apostar ou não
            if (str(p.card1.name) == data[0]) and (str(p.card2.name) == data[1]) or (str(p.card1.name) == data[1]) and (str(p.card2.name) == data[0]):
                if (data[2] == "blue") or (data[2] == "green") or (data[2] == "yellow"):
                    if (p.money >= 100*int(count)): # condição de all-in
                        return 100*int(count)
                    else:
                        return p.money
                elif (data[2] == "red") :
                    return 0
    else:
        return 0

def median(p,count):
    # importa tabela de mãos iniciais para uma lista
    with open('initial-hands.csv', newline='') as f:
        reader = csv.reader(f)
        datas = list(reader)
    count = count/10 + 1 # Aumenta as apostas a cada 10 rodadas
    if p.money > 0:
        for data in datas:
            # Verifica na tabela de mãos iniciais qual é a mão do jogador e se ele irá apostar ou não
            if (str(p.card1.name) == data[0]) and (str(p.card2.name) == data[1]) or (str(p.card1.name) == data[1]) and (str(p.card2.name) == data[0]):
                if (data[2] == "blue") or (data[2] == "green"):
                    if (p.money >= 100*int(count)): # condição de all-in
                        return 100*int(count)
                    else:
                        return p.money
                elif (data[2] == "red")  or (data[2] == "yellow"):
                    return 0
    else:
        return 0

def passive(p,count):
    # importa tabela de mãos iniciais para uma lista
    with open('initial-hands.csv', newline='') as f:
        reader = csv.reader(f)
        datas = list(reader)
    count = count/10 + 1 # Aumenta as apostas a cada 10 rodadas
    if p.money > 0:
        for data in datas:
            # Verifica na tabela de mãos iniciais qual é a mão do jogador e se ele irá apostar ou não
            if (str(p.card1.name) == data[0]) and (str(p.card2.name) == data[1]) or (str(p.card1.name) == data[1]) and (str(p.card2.name) == data[0]):
                if (data[2] == "blue"):
                    if (p.money >= 100*int(count)): # condição de all-in
                        return 100*int(count)
                    else:
                        return p.money
                elif (data[2] == "red") or (data[2] == "green") or (data[2] == "yellow"):
                    return 0
    else:
        return 0
