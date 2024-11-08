#include <stdio.h>
int main(){
	int customer_ID;
	char customer_name;
	int units_consumed;
	float charges_per_unit;
	float total_amount_to_pay;
	//prompt the user to enter
	printf("enter the customer ID:");
	scanf("%d",&customer_ID);
	
	printf("enter the customer name \n:");
	scanf("%c",&customer_name);
	
if(units_consumed <199){
	charges_per_unit=1.20;
	total_amount_to_pay=units_consumed*charges_per_unit;
	printf("total amount to pay:");
	scanf("%f",&total_amount_to_pay);
}
     else if(units_consumed 200<400){
	charges_per_unit=1.50;
	total_amount_to_pay=units_consumed*charges_per_unit;
	printf("total amount to pay:");
	scanf("%f",&total_amount_to_pay);
}
     else if(units_consumed 400<600){
	charges_per_unit=1.80;
	total_amount_to_pay=units_consumed*charges_per_unit;
	printf("total amount to pay:");
	scanf("%f",&total_amount_to_pay);
}
else(units_consumed 600 ){
	charges_per_unit=2.00;
	total_amount_to_pay=units_consumed*charges_per_unit;
	printf("total amount to pay:");
	scanf("%f",&total_amount_to_pay);
}
	//the minimum bill should be 100
	
	
	
	
	
	//if the bill exceeds 400 then a surcharging of 15% will be charge 
	
	
	return 0;
}