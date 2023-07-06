from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    # Testes para a função encrypt_message
    # testa com a key maior do que a length da mensagem
    assert encrypt_message("abcd", 99) == "dcba"
    # testa com a key menor do que 0
    assert encrypt_message("dcba", -99) == "abcd"
    # testa com a key igual a 0
    assert encrypt_message("abcd", 0) == "dcba"
    # testa com a key igual a length da mensagem
    assert encrypt_message("abcdf", 5) == "fdcba"
    # testa caso de sucesso do caso impar
    assert encrypt_message("abcdefg", 3) == "cba_gfed"
    # testa caso de sucesso do caso par
    assert encrypt_message("abcdef", 4) == "fe_dcba"
    # testa caso de erro do caso par
    assert encrypt_message("abcdef", 2) != "cba_efd"
    # # testa caso de erro do caso impar
    assert encrypt_message("abcdef", 3) != "cab_fed"
    # # testa o caso se em vez de inverter, ordena com a key maior que length
    assert encrypt_message("cdba", 5) != "abcd"
    # testa o caso de passar uma string vazia como mensagem
    assert encrypt_message("", 3) == ""
    # testa o caso de passar uma key valida, se eles são realmente separados
    assert encrypt_message("abcdef", 3) != "cbafed"

    with pytest.raises(TypeError):
        encrypt_message(123, 5)
        encrypt_message("abcd", "abc")
