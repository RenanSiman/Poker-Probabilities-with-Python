from poker import Carta

def checar_sequencia(mao, jogador):
    comb = [mao,jogador]
    for i in range(len(comb)):
        if jogador