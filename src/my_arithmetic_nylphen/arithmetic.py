"""Fonctions arithmétiques de base."""


def pgcd(a: int, b: int) -> int:
    """Calcule le plus grand commun diviseur de deux entiers.

    Le calcul utilise l'algorithme d'Euclide sur les valeurs absolues
    des arguments : le résultat est donc toujours positif ou nul.

    Parameters
    ----------
    a : int
        Premier entier (peut être négatif ou nul).
    b : int
        Second entier (peut être négatif ou nul).

    Returns
    -------
    int
        Le plus grand commun diviseur de `a` et `b`. Par convention,
        ``pgcd(0, 0)`` vaut ``0``.

    Raises
    ------
    TypeError
        Si `a` ou `b` n'est pas un entier (les booléens sont refusés).

    See Also
    --------
    math.gcd : équivalent de la bibliothèque standard.

    Examples
    --------
    >>> pgcd(12, 18)
    6
    >>> pgcd(-12, 18)
    6
    >>> pgcd(0, 5)
    5
    """
    if not isinstance(a, int) or not isinstance(b, int) or isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("pgcd attend deux entiers")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
