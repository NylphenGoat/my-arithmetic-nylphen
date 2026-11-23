import math

import pytest

from my_arithmetic_nylphen import pgcd


@pytest.mark.parametrize(
    ("a", "b", "attendu"),
    [
        (12, 18, 6),
        (18, 12, 6),
        (17, 5, 1),
        (100, 10, 10),
        (7, 7, 7),
        (1, 999, 1),
    ],
)
def test_pgcd_cas_simples(a, b, attendu):
    assert pgcd(a, b) == attendu


def test_pgcd_avec_zero():
    assert pgcd(0, 5) == 5
    assert pgcd(5, 0) == 5
    assert pgcd(0, 0) == 0


def test_pgcd_nombres_negatifs():
    assert pgcd(-12, 18) == 6
    assert pgcd(12, -18) == 6
    assert pgcd(-12, -18) == 6


def test_pgcd_grands_nombres():
    assert pgcd(2**40 * 3, 2**35 * 5) == 2**35


def test_pgcd_coherent_avec_math_gcd():
    for a in range(-30, 31):
        for b in range(-30, 31):
            assert pgcd(a, b) == math.gcd(a, b)


@pytest.mark.parametrize(("a", "b"), [(1.5, 3), (3, "6"), (None, 2), (True, 4)])
def test_pgcd_refuse_non_entiers(a, b):
    with pytest.raises(TypeError):
        pgcd(a, b)
