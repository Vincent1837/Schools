import java.sql.SQLOutput;
import java.util.Scanner;
public class A6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int inputNumber = sc.nextInt();
            if (inputNumber == -1) {
                break;
            }
            System.out.println(function(inputNumber));
        }
    }
    public static int function(int number) {
        if (number <= 4){
            return 3;
        } else if (number <= 9){
            return 2 + function(number - 2);
        } else {
            return 1 + function(number-22) + function(function(number-30)-30);
        }
    }
}
