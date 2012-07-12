def karakter_fiLtre(dosya_adi,n):
	dosya = open (dosya_adi,"r")
	for i in dosya:
		i = i.strip()
		for j in i:
			if j == n:
				break
		if j != n and j == i[len(i) -1]:
			print i
