#include <stdio.h>
#include <conio.h>
int main(){
	FILE *pf;
	character[100];
	pf=fopen("data.txt","W");
	if(pf==NULL){
		printf("unable to open the file");
	}else{
		printf("enter a sentence");
		gets(inputs);
		fputs(inputs,pf);
		fclose(pf);
	}
	getch();
	return 0;
}