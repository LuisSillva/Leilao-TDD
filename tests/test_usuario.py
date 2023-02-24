from src.leilao.excecoes import LanceInvalido
from src.leilao.dominio import Leilao, Usuario

import pytest

@pytest.fixture
def vini():
    return Usuario('Vini', 100.0)

@pytest.fixture
def leilao():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_deve_permitir_propor_lance_quando_o_valor_e_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 10.0)

    assert vini.carteira == 90.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):
    
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 200.0)
