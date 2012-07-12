def bosLuk_birak_tekrarLa(sozcuk, bosluk_uzunlugu, tekrar_sayisi):
        if (bosluk_uzunlugu == 0):
                print sozcuk * tekrar_sayisi 
        else:
                bosluk = ' ' * (bosluk_uzunlugu - 2)
                for sefer in range(tekrar_sayisi - 1) :
                        print sozcuk,bosluk,
                print sozcuk
