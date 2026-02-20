import java.util.Random;
import java.util.Scanner;
//java dice roller
//declaration of variables
//get # of dice from the users
//check if number of diCE>0
//get the total
//display ascii of dice

public class gaucho {

   public static void main(String[] args) {
      Scanner scanner=new Scanner(System.in);
      Random random=new Random();
      int numdice;
      int total=0;
      System.out.println("enter the number of dice:");
      numdice=scanner.nextInt();
      if (numdice>0) {
         for (int i = 0; i <numdice; i++) {
            int roll=random.nextInt(1,7);
            printdice(roll);
         
            System.out.println("you rooled "+roll);
            total=total+roll;

            
         }
         System.out.println("total:"+total);


         
      }else{
         System.out.println("NO. of dice must be more than zero");
      }



   



      scanner.close();

      
      
   }
   static void printdice(int roll){
      String dice1="""
            -------
            |           |
            |    ֎      |
            |           |
             -------

            """;
              String dice2="""
            -------
            | ֎         |
            |    ֎      |
            |           |
             -------

            """;
                 String dice3="""
            -------
            | ֎         |
            |    ֎      |
            |         ֎   |
             -------

            """;
                 String dice4="""
            -------
            | ֎             |
            |    ֎          |
            |  ֎        ֎   |
             -------

            """;
                 String dice5="""
            -------
            | ֎             |
            |    ֎       ֎  |
            |   ֎       ֎   |
             -------

            """;
                 String dice6="""
            -------
            | ֎            ֎|
            |    ֎         ֎|
            |  ֎        ֎   |
             -------

            """;
            
            
            System.out.println(dice1);
            switch (roll) {
               case 1 -> System.out.println(dice1);
               case 2 -> System.out.println(dice2);
               case 3 -> System.out.println(dice3);
               case 4 -> System.out.println(dice4);
               case 5 -> System.out.println(dice5);
               case 6 -> System.out.println(dice6);
               
                  
               
            
               default -> System.out.println("invalid roll");
                  
            }


   }
}