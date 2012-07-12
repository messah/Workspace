def histogram(cumle):
    depo = dict()
    sayac=0
    kelime = str.split(cumle)
    for i in range(0, len(kelime)):
        depo[kelime[i]] = sayac
        
