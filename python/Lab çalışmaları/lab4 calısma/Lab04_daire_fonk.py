import math
def daire_fonk(r):
    if r < 0:
        print "düzgün sayý gir"
    else:
        alan=(math.pi)*r*r
        cevre=2*r*(math.pi)
        print "alan= %f \ncevre= %f "%(alan,cevre)
