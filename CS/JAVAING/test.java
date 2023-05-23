import java.util.InputMismatchException;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {
        int first_number, second_number;
        String operator;
    
        Scanner sc =  new Scanner(System.in);
        System.out.println("Enter the first number: ");
        while (true) {
            try {
                first_number = sc.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Invalid numnber! Please enter again: ");
            }
        }
        System.out.println("Enter the operator (+, -, *, or /): ");
        while (true) {
            try {
                first_number = sc.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Invalid operator! Please enter again: ");
            }
        }
        System.out.println("enter the second number: ");
        while (true) {
            try {
                first_number = sc.nextInt();
                break;
            } catch (Exception e) {
                System.out.println("Invalid numnber! Please enter again: ");
            }
        }
        sc.close();
    } 
    public int getNumber (Scanner sc) {
        String input_string = sc.nextLine();
        if ()
        
        
        return ;
    }
    public String getOperator (Scanner sc) {

    }

    public boolean isDigit (String s) {
        for (int i = 0; i < s.length(); i++) {
            if (48 <= s.charAt(i) && 57 >= s.charAt(i) || s.charAt(i) == 46) {
                return true;
            }
            return false;
        }
    }
}
