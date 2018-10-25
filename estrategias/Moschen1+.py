# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
    def __init__(self):
        self.hist_jogadores = []
    
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        self.hist_jogadores.append(len(reputacoes_dos_jogadores))
        quant_jogadores = len(reputacoes_dos_jogadores)
        if quant_jogadores > (self.hist_jogadores[0])/4:
            if rodada%2 == 1:
                escolhas = ['c']*quant_jogadores
            else:
                escolhas = ['d']*quant_jogadores
            return escolhas
        else:
            if reputacao_atual > 0.45:
                escolhas = ['d']*quant_jogadores
            else: 
                escolhas = ['c']*quant_jogadores
            return escolhas 
                
            
            
            
