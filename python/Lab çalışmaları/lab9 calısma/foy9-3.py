dosya = open ("words.txt","r")
top = 0
for i in dosya:
	i = i.strip()
	list_i = list(i)
	list_i.sort()
	new = ''
	new = new.join(list_i)
	if i == new:
		print i
		top +=1
print "\n\nAlfabetik kelime sayisi : " ,top
