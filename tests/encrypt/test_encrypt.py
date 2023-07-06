from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("abcd", 5) == "dcba"
    assert encrypt_message("abcd", -4) == "dcba"
    assert encrypt_message("abcd", 4) == "dcba"
    assert encrypt_message("abcdef", 3) == "cba_fed"
    assert encrypt_message("abcd", 2) == "dc_ba"
    assert encrypt_message("abcdef", 3) != "cab_fed"
    assert encrypt_message("abcd", 5) != "abcd"
    assert encrypt_message("cdba", 5) != "abcd"
    assert encrypt_message("", 3) == ""

    with pytest.raises(TypeError):
        encrypt_message(123, 5)
        encrypt_message("abcd", "abc")
