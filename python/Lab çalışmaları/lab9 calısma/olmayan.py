try:
         fin = open('oLmayan_bir_dosya.txt')
         for Line in fin:
                  print Line
         fin.close()
except:
     print 'Bir hata olustu.'
     
