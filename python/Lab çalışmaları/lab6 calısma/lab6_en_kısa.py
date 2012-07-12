def en_kisa_keLime(cumle):
    depo = dict()
    kelime = str.split(cumle)
    for i in range(0, len(kelime)):
        depo[kelime[i]] = len(kelime[i])
    en_kisa = depo[kelime[0]]
    j = 0
    for i in range(0, len(kelime)):
        if depo[kelime[i]] <= en_kisa:
            j = i
            en_kisa = depo[kelime[i]]
    print "En kisa : ", kelime[j], "\nUzunluk : ", depo[kelime[j]]
