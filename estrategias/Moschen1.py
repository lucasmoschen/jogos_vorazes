# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        if rodada%2 == 1:
            escolhas = ['c']*len(reputacoes_dos_jogadores)
        else:
            escolhas = ['d']*len(reputacoes_dos_jogadores)
        return escolhas

