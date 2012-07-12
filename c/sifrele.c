#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *sifrele(char *dizi,int *artim)
{
	int i,k;
	int n;
	for(i = 0,k = 0;i < strlen(dizi) && k < strlen(dizi);i++,k++ ){
		n = *(dizi + i);
		n += *(artim + k);
		*(dizi + i) = n;
	}
	printf("\n");
	return dizi;	
}
char *sifrecoz(char *dizi,int *artim)
{
	
	int i,k;
	int n;
	for(i = 0,k = 0;i < strlen(dizi) && k < strlen(dizi);i++,k++){
		n = *(dizi + i);
		n -= *(artim + k);
		*(dizi +i) = n;	
	}
	printf("\n");
	return dizi;
}

int main()
{
	int sayac[] = {1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3};
	char sozcuk[] = "cin ali";
	printf("orjinal sozcuk : %s\n",sozcuk);
	char *sifreli = sifrele(sozcuk,sayac);
	printf("sifrelenmis sozcuk : %s\n",sifreli);
	char *cozulmus = sifrecoz(sozcuk,sayac);
	printf("cozulmus sozcuk : %s\n",cozulmus);
	getchar();
	return 0;
}
