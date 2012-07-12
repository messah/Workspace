import math
def kok_hesapla(a,b,c):
    disk=(b*b)-4*a*c
    
    if (disk<0):
        print 'kök yok'
    else:
        print "1.kök=",((-b)+math.sqrt(b*b-4*a*c))/2*a
        print "2.kök=",((-b)-math.sqrt(b*b-4*a*c))/2*a
