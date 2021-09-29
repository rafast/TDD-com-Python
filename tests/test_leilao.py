from unittest import TestCase

from dominio import Usuario, Lance, Leilao
from excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self) -> None:
        self.rafa = Usuario('Rafael', 500.0)
        self.jaq = Usuario('Jaqueline', 500.0)
        self.lance_do_rafa = Lance(self.rafa, 100.0)
        self.lance_da_jaq = Lance(self.jaq, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(self.lance_da_jaq)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):

            self.leilao.propoe(self.lance_da_jaq)
            self.leilao.propoe(self.lance_do_rafa)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_da_jaq)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        leo = Usuario('Leonardo', 500.0)
        lance_do_leo = Lance(leo, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(self.lance_da_jaq)
        self.leilao.propoe(lance_do_leo)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    # Se o leilao nao tiver lances, deve permitir propor lance

    def test_deve_permitir_propor_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_rafa)
        quantidade_de_lances_recebida = len(self.leilao.lances)

        self.assertEqual(1, quantidade_de_lances_recebida)

    # Se o ultimo usuario for diferente, deve permitir propor lance
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_rafa)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebido)
    # Se o ultimo usuario for o mesmo, nao deve permitir propor lance
    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_rafa200 = Lance(self.rafa, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_rafa)
            self.leilao.propoe(lance_do_rafa200)