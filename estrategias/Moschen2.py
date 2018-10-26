# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador


class MeuJogador(Jogador):

    def __init__(self):
        self._name = "Moschen2"
        self.hist_comida = []
        self.n_inicial_jogadores = 0
        
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        self.hist_comida.append(comida_atual)
        n_jogadores = len(reputacoes_dos_jogadores)
        if rodada == 1:
            self.n_inicial_jogadores = n_jogadores
        if n_jogadores > self.n_inicial_jogadores/4:
            if rodada%2 == 1:
                escolhas = ['c']*n_jogadores
            else:
                escolhas = ['d']*n_jogadores
            return escolhas
        else: 
            if reputacao_atual > 0.4:
                escolhas = ['d']*n_jogadores
            else:
                escolhas = ['c']*n_jogadores
            return escolhas
        
    def resultado_da_cacada(self, comida_ganha):
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        print(self.hist_comida[-1])