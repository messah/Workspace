import math
def mutLak_geneL():
    secenek=input("Karmas�k say�lar i�in 1, tamsay�lar i�in 2, ondal�kl� say�lar i�in 3, ��kmak i�in 4 giriniz:")
    if (secenek == 1):
        r=input("Ger�el k�sm� giriniz :")
        a=input("Sanal k�sm� (i' nin katsay�s�n�) giriniz :")
        print "Kompleks say�n�n mutlak de�eri :",math.sqrt(a**2+r**2)
    elif (secenek==2):
        b=input("Tamsay�y� giriniz:")
        print "Tamsay�n�n mutlak de�eri :", int(math.fabs(b))
    elif (secenek==3):
        c=input("Ondal�kl� say�y� giriniz:")
        print "Ondal�kl� say�y� giriniz:", math.fabs(c)
    elif (secenek==4):
        print "lan ne yapt�n ;c�kt�n ya!!!"
        
