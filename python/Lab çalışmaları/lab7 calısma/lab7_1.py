import doctest
def ardisik_topLam(n):
    """
    >>> ardisik_topLam(7)
    28
    >>> ardisik_topLam(0)
    Lütfen pozitif bir tamsayı giriniz.
    >>> ardisik_topLam(-7)
    Lütfen pozitif bir tamsayı giriniz.
    >>> ardisik_topLam(7.1)
    Lütfen pozitif bir tamsayı giriniz.
    """
    sonuc=0
    if (n==0) | (n < 0) | (n!=round(n+0.4)):
        print "Lütfen pozitif bir tamsayı giriniz."
    else:
        for i in range(1,n+1):
            sonuc+=i
        return sonuc
doctest.testmod()
