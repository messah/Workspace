import doctest
def diziden_arindir(kisa_dizi, uzun_dizi):
    """
    >>> diziden_arindir('an', 'banana')
    ba
    >>> diziden_arindir('cyc', 'bicycle')
    bile
    >>> diziden_arindir('iss', 'Mississippi ')
    Mippi
    >>> diziden_arindir('eggs', 'bicycle')
    bicycle
    """
    yeni=""
    index = 0
    while index < len(uzun_dizi):
        if (kisa_dizi[0] == uzun_dizi[index]) & (kisa_dizi in uzun_dizi[index:]):
                index += len(kisa_dizi)
        yeni += uzun_dizi[index]
        index += 1
    print yeni
doctest.testmod()
