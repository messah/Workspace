
sayi = rand(100)
i=0
while (1)
	i += 1
	puts("Tahmininizi giriniz")
	girdi = gets
	new = girdi.to_i
	if new == sayi and i < 10
		puts ("sayiyi buldun")
		break
	end
	if new != sayi and i < 10
		puts ("sayiyi arttirin") if new < sayi
		puts ("sayiyi azaltin")  if new > sayi
	end
	if i == 10
		puts ("sayiyi bulamadiniz")
		break
	end
end
