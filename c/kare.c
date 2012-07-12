/* '*'ler kullanarak kenar uzunlugu verilen kareyi cizer */

#include<stdio.h>
int main( void ) 
{
	int kenar;
	int i;
	int j;
	
	printf("Karenin kenar uzunlugu: ");
	scanf("%d", &kenar);
	
	/* Gecerli bir deger mi */
	while((kenar < 0) || (kenar > 20)) {
	
		printf("Lutfen 0 ile 20 arasinda bi deger giriniz.");
		printf("Karenin kenar uzunlugu");
		scanf("%d", &kenar);
	}
	
	/* karenin cizilmesi */
	for(i = 1; i <= kenar; i++) {
	
		if(kenar == 0)
			break;
		
		/* alt ve üst kenarlarin cizimi */
		if((i == 1) || (i == kenar)) {
		
			for(j = 1; j <= kenar; j++)
				printf("*");
			printf("\n");
			continue;
		} /* if sonu */
		
		/* sag ve sol kenarlarin cizimi */
		for(j = 1; j <= kenar; j++)
			if((j == 1) || (j == kenar))
				printf("*");
			else
				printf(" ");
		
		printf("\n");
	} /* for sonu */
	
	return 0;
}
