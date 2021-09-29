from dominio import Usuario, Leilao

import pytest

from excecoes import LanceInvalido


@pytest.fixture
def rafa():
    return Usuario('Rafa', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(rafa, leilao):
    rafa.propoe_lance(leilao, 50.0)

    assert rafa.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(rafa, leilao):
    rafa.propoe_lance(leilao, 5.0)

    assert rafa.carteira == 95.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(rafa, leilao):
    rafa.propoe_lance(leilao, 100.0)

    assert rafa.carteira == 0.0

def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(rafa, leilao):
    with pytest.raises(LanceInvalido):

        rafa.propoe_lance(leilao, 200.0)
