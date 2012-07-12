def aLfabetik_artan(sozcuk):
    liste = list(sozcuk)
    liste.sort()
    yeni_liste = ''
    yeni_liste = yeni_liste.join(liste)
    if yeni_liste == sozcuk:
        print True
    else:
        print False
