# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    def __init__(self):
        hist_jogadores = []
    
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        hist_jogadores.append(len(reputacoes_dos_jogadores))
        if len(reputacoes_dos_jogadores) > hist_jogadores[0]/4:
            if rodada%2 == 1:
                escolhas = ['c']*len(reputacoes_dos_jogadores)
            else:
                escolhas = ['d']*len(reputacoes_dos_jogadores)
            return escolhas
        else:
            if reputacao_atual > 0.45:
                escolhas = ['d']*len(reputacoes_dos_jogadores)
            else: 
                escolhas = ['c']*len(reputacoes_dos_jogadores)
            return escolhas 
                
            
            
            
