import math
def mutLak_geneL():
    secenek=input("Karmasýk sayýlar için 1, tamsayýlar için 2, ondalýklý sayýlar için 3, çýkmak için 4 giriniz:")
    if (secenek == 1):
        r=input("Gerçel kýsmý giriniz :")
        a=input("Sanal kýsmý (i' nin katsayýsýný) giriniz :")
        print "Kompleks sayýnýn mutlak deðeri :",math.sqrt(a**2+r**2)
    elif (secenek==2):
        b=input("Tamsayýyý giriniz:")
        print "Tamsayýnýn mutlak deðeri :", int(math.fabs(b))
    elif (secenek==3):
        c=input("Ondalýklý sayýyý giriniz:")
        print "Ondalýklý sayýyý giriniz:", math.fabs(c)
    elif (secenek==4):
        print "lan ne yaptýn ;cýktýn ya!!!"
        
