def kiyasla(sayi_1,sayi_2):
    if (sayi_1 > sayi_2):
        return 1
    elif (sayi_1 == sayi_2):
        return 0
    elif (sayi_1 < sayi_2):
        return -1

def isaret_kontroL(sayi_1, sayi_2):
    if((sayi_1 * sayi_2)>0):
        return 1
    elif ((sayi_1 * sayi_2)<0):
        return -1
    elif ((sayi_1 * sayi_2)==0):
        return 0

def fonk_geneL(fonk_isim,sayi_1,sayi_2):
    return fonk_isim(sayi_1,sayi_2)
