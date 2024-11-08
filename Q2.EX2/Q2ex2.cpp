#include<stdio.h>
#include<conio.h>
int main(){
	FILE*pf;
	char names[5];
	int marks;
	pf=fopen("name_marks","a");
	if(pf==NULL){
		printf("unable to open the file");
		
	}else{
		printf("data excutes succefully");
	}
	
	








getch();
return 0;
}