//c structures
#include <stdio.h>
//strcpy
#include <string.h>
 
  



struct student 
{
   char name [30];
   char email [30];
   int phone;
   int ID_number;
   char reg_no[15];
   
   
   
   int marks;
   float height;	
}student1,student2;
int main()
{
    // struct student, student1,student 2
	 
		 
	 //strcpy(student1.name,"james");
	 //prompt the user to enter
	 printf("enter your name:");
	 scanf("%s",&student1.name);
	 
	 student1.height=5.7;
	 strcpy(student1.reg_no,"CT101/G/23054/24");
	 strcpy(student1.email,"emmayancondric@gmail.com");
	 student1.phone=252657647;
	 
	 printf("name: %s\n",student1.name);
	 
	 printf("height:%f  \n",student1.height);
	 
	 printf("reg_no",student1.reg_no);
	 
	 printf("email:%s \n",student1.email);
	 
	 printf("phone: %s \n",student1.phone);
	 
	 
	return 0;
}