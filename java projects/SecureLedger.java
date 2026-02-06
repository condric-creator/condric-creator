import java.util.Scanner; 

public class SecureLedger {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
       
        String secretPassword = "crypto2026"; 
        int attempts = 0;
        int maxAttempts = 3;
        boolean accessGranted = false;

        System.out.println("--- SECURE CRYPTO TERMINAL ---");


        while (attempts < maxAttempts) {
            System.out.print("Enter Access Key: ");
            String input = scanner.nextLine();

            
            if (input.equals(secretPassword)) {
                accessGranted = true;
                break;}
            else{    

                attempts++;
                System.out.println("ACCESS DENIED. Attempts left: " + (maxAttempts - attempts));
            }
        }


        if (accessGranted) {
            System.out.println("\nWELCOME BACK, TRADER.");
           
        } else {
            System.out.println("\n[!] SYSTEM LOCKDOWN: UNAUTHORIZED ACCESS DETECTED.");
        }

        scanner.close();
    }
}