import doctest
def kiyasla(sayi_1,sayi_2):
    """
    >>> kiyasla(9,4)
    1
    >>> kiyasla(6,6)
    0
    >>> kiyasla(3,13)
    -1
    """
    if (sayi_1 > sayi_2):
        return 1
    elif (sayi_1 == sayi_2):
        return 0
    elif (sayi_1 < sayi_2):
        return -1
doctest.testmod()
