 #include<stdio.h>
 #include<conio.h>
 int main(){
 	FILE*pf;
 	char name[5];
 	int marks;
 	//prompt the user to enter
 	printf("enter your name:\n");
 	scanf("%c",&name);
 	//prompt the user to enter
 	printf("enter your marks: \n");
 	scanf("%d",&marks);
 	if(pf==NULL){
		 printf("unable to open this file");
	 }else{
		 fprintf(pf,"%s\t",name);
		 fprintf(pf,"%d",marks);
		 
		 
         printf("data written successfully");
         fclose(pf);
	 }
	 getch();
	 return 0;
 }
 	
 	
 	