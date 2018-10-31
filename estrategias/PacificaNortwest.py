from estrategias.jogadores import Jogador
import math
import random

class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        escolhas=[]
        
        for k in reputacoes_dos_jogadores:
            if rodada==1:
                escolhas.append('c')
            else:
                if rodada<400:
                    if reputacao_atual>0.5:
                        escolhas.append('d')
                    else:
                        escolhas.append('c')
                else:
                    if sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)<0.5: #media reputação
                        escolhas.append('d')
                    else:
                        escolhas.append('c')
        return escolhas
            