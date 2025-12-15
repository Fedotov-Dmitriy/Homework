
import pytest
from hamming import decrypt, encrypt


def test_encrypt_returns_only_0_1():
    enc = encrypt("A")
    assert set(enc) <= {"0", "1"}


def test_decrypt_no_error_is_minus_one():
    enc = encrypt("A")
    assert decrypt(enc) == -1


def test_decrypt_finds_error_bit_0():
    enc = encrypt("A")
    bad = ("1" if enc[0] == "0" else "0") + enc[1:]
    assert decrypt(bad) == 0


def test_decrypt_finds_error_last_bit():
    enc = encrypt("A")
    bad = enc[:-1] + ("1" if enc[-1] == "0" else "0")
    assert decrypt(bad) == len(enc) - 1


def test_decrypt_wrong_length_raises():
    with pytest.raises(ValueError):
        decrypt("0101")  # не кратно 7
