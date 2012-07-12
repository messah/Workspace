import os
sayac = 0
for i in (os.listdir(os.getcwd())):
	if os.path.isdir(os.path.abspath(i)):	
		sayac += 1
		
print sayac
