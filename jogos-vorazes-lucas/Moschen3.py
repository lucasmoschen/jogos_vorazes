# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

import numpy as np


class MeuJogador(Jogador):

    def __init__(self):
        pass

    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        media = np.mean(reputacoes_dos_jogadores) 
        desvpad = np.std(reputacoes_dos_jogadores)
        t = np.random.normal(media,desvpad)
        escolhas = []
        for rep in reputacoes_dos_jogadores:
            if rep <= t:
                escolhas.append('d')
            else:
                escolhas.append('c')
        return escolhas

    def resultado_da_cacada(self, comida_ganha):
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        pass

