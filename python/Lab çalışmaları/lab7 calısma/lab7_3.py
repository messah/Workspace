def sondan_basa_yaz(s):
    tip=type(s)
    if tip !=str:
        print "Lütfen parametre olarak karakter dizisi giriniz."
    else:
        turkce="Ç, ç, Ğ, ğ, ı, Đ, Ö, ö, Ş, ş, Ü, ü"
        ters=""
        n=len(s)
        for kelime in s:
            if kelime not in turkce:
                ters=ters+kelime
        print "'",
        while n:
            print s[n-1],
            n -= 1
        print "'"
