def tc_no_dogruLa(kimlik_no):
	top1,top2,top3  = 0,0,0
	skimlik_no = str (kimlik_no)
	if kimlik_no > 0 & type(kimlik_no) == long & len (skimlik_no) == 11:
		for i in range (9):
			if (i % 2 == 0):
				top1 += int (skimlik_no[i])*7
			else:
				top2 += int (skimlik_no[i])
		on = (top1 -top2) % 10
		for i in range (10):
			top3 += int(skimlik_no[i])
		if int(skimlik_no[9]) == on and int (skimlik_no[10]) == (top3 % 10):
			print "TC kimlik numarasi gecerlidir"
		else:
			print "TC kimlik numarasi gecerli degildir"
	else:
		print "Lutfen 11 basamakli bir tamsayi giriniz"
