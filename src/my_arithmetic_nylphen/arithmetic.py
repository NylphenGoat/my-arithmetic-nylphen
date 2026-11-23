"""Fonctions arithmétiques."""


def pgcd(a: int, b: int) -> int:
    """Retourne le plus grand commun diviseur de a et b (algorithme d'Euclide).

    Le résultat est toujours positif ou nul ; pgcd(0, 0) vaut 0.
    """
    if not isinstance(a, int) or not isinstance(b, int) or isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("pgcd attend deux entiers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
