import doctest
def karakterden_arindir(karakter, kar_dizisi):
    """
    >>> karakterden_arindir('a', 'apple')
    pple
    >>> karakterden_arindir('a', 'banana')
    bnn
    >>> karakterden_arindir('z', 'banana')
    banana
    >>> karakterden_arindir('i', 'Mississippi')
    Msssspp
    """
    yeni=""
    index = 0
    while index < len(kar_dizisi):
        if karakter != kar_dizisi[index]:
            yeni+=kar_dizisi[index]
        index += 1
    print yeni
doctest.testmod()
