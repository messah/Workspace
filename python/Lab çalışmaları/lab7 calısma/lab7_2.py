def yariLar_topLami(n):
    toplam=0
    yedek=n
    sayac=0
    if (n==0) | (n < 0) | (n!=round(n+0.4)):
        print "Lütfen pozitif bir tamsayı giriniz."
    else:
        n=n/2.0
        while (0.1 <= n) & (sayac < yedek):
            toplam+=n
            n=n/2.0
            sayac+=1
        return toplam
