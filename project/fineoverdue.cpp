
 
 #include<stdio.h>
 int main(){
 int book_id;
 int due_date;
 int return_date;
 int fine_rate;
 int fine_amount;
 int days_overdue;

 //prompt the user to enter

printf("book_id \n");
scanf("%d",&book_id);

printf("due_date \n");
scanf("%d",&due_date);

printf("return_date \n");
scanf("%d",&return_date);

printf("days_overdue \n");
scanf("%d",&days_overdue);

printf("fine_rate \n");
scanf("%d",&fine_rate);

printf("fine_amount \n");
scanf("%d",&fine_amount);
 //calculate days _overdue
days_overdue =(return_date-due_date);
if(days_overdue<=7){
	fine_rate=20;
	fine_amount=days_overdue*fine_rate;
	printf("the fine_amount:%d",fine_amount);
	
}
else(days_overdue<15);{
	fine_rate=20;
	fine_amount=days_overdue*fine_rate;
	printf("the fine_amount is:%d",fine_amount);
}	
 else();{
	fine_rate=10;
	fine_amount=days_overdue*fine_rate;	
	printf("the fine_amount is:%d",fine_amount);

 }
return 0;
	
 }