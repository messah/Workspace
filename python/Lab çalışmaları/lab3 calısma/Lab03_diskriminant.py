import math
def kok_hesapla(a,b,c):
    disk=(b*b)-4*a*c
    
    if (disk<0):
        print 'k�k yok'
    else:
        print "1.k�k=",((-b)+math.sqrt(b*b-4*a*c))/2*a
        print "2.k�k=",((-b)-math.sqrt(b*b-4*a*c))/2*a
