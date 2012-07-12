def yoL_secici(x, y, z):
    a = b = c = d = e = f = g = 0
    if x ==0 & y==0 & z==0:
        a = 0
    elif (x ==0) & (y==0) & (z==1):
        a = 1
    elif (x ==0) & (y==1) & (z==0):
        b = 1
    elif (x ==0) & (y==1) & (z==1):
        c = 1
    elif (x ==1) & (y==0) & (z==0):
        d = 1
    elif (x ==1) & (y==0) & (z==1):
        e = 1
    elif (x ==1) & (y==1) & (z==0):
        f = 1
    elif (x ==1) & (y==1) & (z==1):
        g = 1
    print "a : ",a
    print "b : ",b
    print "c : ",c
    print "d : ",d
    print "e : ",e
    print "f : ",f
    print "g : ",g
