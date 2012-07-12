dosya = open ("sozcuk.txt","r")
for i in dosya:
	i = i.strip()
	if len(i) > 5:
		print i
