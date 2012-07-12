import time
import doctest
def faktoriyeL(tamsayi):

   start = time.clock()
   """
   >>> faktoriyeL(9)
   362880
   >>> faktoriyeL(4)
   24
   >>> faktoriyeL(1)
   1
   >>> faktoriyeL(0)
   1
   >>> faktoriyeL(-8)
   Negatif tamsayilarin faktoriyel hesaplamasi yapilamaz.
   """

   fakt=1
   if((tamsayi==0) | (tamsayi==1)):
       return 1
   elif(tamsayi<0):
       print "Negatif tamsayilarin faktoriyel hesaplamasi yapilamaz."
       return 
   else:
       while (tamsayi>0):
           fakt*=tamsayi
           tamsayi-=1
   end = time.clock()
   print "%.5f  %.5f  %.5f"%(start,end,end - start)
   return fakt
doctest.testmod()
