from gasp import *
import time

def bocek(x_koord, y_koord):
	i=x_koord
	j=y_koord
	Circle((i,j), 40,filled = True,color = (21,38,208))
	Circle((i-20,j+35), 10,filled = True,color = (255,255,255))
	Circle((i+20,j+35), 10,filled = True,color = (255,255,255))
	Circle((i-19,j+33), 5,filled = True,color = (208,53,39))
	Circle((i+20,j+33), 5,filled = True,color = (208,53,39))
	Circle((i+5,j-95), 80,filled = True,color = (80,208,60))

r = 2 #istenen degergirilecek

begin_graphics(background=(0,0,0))
i = 295 #istenen degergirilecek
j = 285 #istenen degergirilecek

if ((i < 0) | (j < 0) ):
	print "yanlis deger girildi !!!!!!!!!!"
else :
	Circle((i/r,j/r), 40/r,filled = True,color = (21,38,208))
	Circle(((i-20)/r,(j+35)/r), 10/r,filled = True,color = (255,255,255))
	Circle(((i+20)/r,(j+35)/r), 10/r,filled = True,color = (255,255,255))
	Circle(((i-19)/r,(j+33)/r), 5/r,filled = True,color = (208,53,39))
	Circle(((i+20)/r,(j+33)/r), 5/r,filled = True,color = (208,53,39))
	Circle(((i+5)/r,(j-95)/r), 80/r,filled = True,color = (80,208,60))

	a = 500 #istenen degergirilecek
	b = 360 #istenen degergirilecek
	bocek(a,b)
sleep(4)
end_graphics()
