import doctest
def kac_basamak(sayi):
    """
    >>> kac_basamak(67853)
    5
    >>> kac_basamak(600)
    3
    >>> kac_basamak(8)
    1
    >>> kac_basamak(0)
    1
    >>> kac_basamak(-8)
    1
    >>> kac_basamak(-9807)
    4
    """
    sayac = 0
    if sayi < 0:
        sayi*= -1
    if sayi == 0:
        return 1
    while sayi > 0:
        sayi /= 10
        sayac += 1

    print sayac
            
doctest.testmod()

