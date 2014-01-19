import unittest
import os
os.chdir('..')
import simulador
from estrategias.jogadores import Jogador


class TesteSimulador(unittest.TestCase):
    def setUp(self):
        self.torneio = simulador.Torneio()


    def testa_instanciacao_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        for i in self.torneio.jogadores.itervalues():
            self.assertIsInstance(i, Jogador)

    def testa_nome_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        self.assertIn('FlavioCoelho', self.torneio.jogadores)

    def testa_propriedade_p(self):
        self.assertEqual(self.torneio.p, 0)
        self.torneio.inicializa_jogadores()
        assert self.torneio.p > 0

    def testa_inicializacao_dos_jogadores(self):
        self.torneio.inicializa_jogadores()
        for dados in self.torneio.historico.itervalues():
            self.assertEqual(dados["reputacao"][-1], 0)
            self.assertEqual(dados["comida"][-1], 300*(self.torneio.p -1))



