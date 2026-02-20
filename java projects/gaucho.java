import java.util.Scanner;
public class gaucho {
    static Scanner scanner=new Scanner(System.in);
       public static void main(String[] args) {
        
        double balance=40000;
        boolean isrunning=true;
        int choice;
        
        while (isrunning) {
            
        
        System.out.println("welcome nanogix bank");
        System.out.println("******************");
        System.out.println("**************");
        System.out.println("******************");
        System.out.println("1.Show balance");
        System.out.println("2. top up the account");
        System.out.println("3.withdral ");
        System.out.println("4.exit");

        System.out.print("Enter the choices(1-4):");
        choice=scanner.nextInt();
        switch (choice) {
            case 1 ->showbalance(balance);
            case 2 ->balance+=deposit();
            case 3 ->balance-=withdral();
            case 4 ->isrunning=true;
            

        
            default ->System.out.println("invalid choice");
        }
    } 
       scanner.close(); 
       }
       static void showbalance(double balance){
        System.out.println(" Balance:"+balance);
       }
       static double deposit(){
        double amount;
        System.out.println("Enter the amount you want to deposit:");
        amount=scanner.nextDouble();
        
         if(amount<0) {
            System.out.print("amount can not be less or equal to zero");
            return 0;
         }
         else{
            return amount;
         } 
       }
       static double withdral(){
         double withdral_amount;
         System.out.println("Enter the amount you want to withdraw:");
         withdral_amount=scanner.nextDouble();
         if (withdral_amount<=0) {
            System.out.println("you can not withdraw money less or equal to zero");

            return 0;   
       
         }else{
            return withdral_amount;
         }

       }
}