import java.util.Locale;
import java.util.Scanner;

public class A2 {
    public static void main(String[] args){
        System.out.println("Input String: ");
        Scanner sc = new Scanner(System.in);
        String inputString = sc.nextLine();
        vowelCounter(inputString);
        sc.close();
    }
    private static void vowelCounter(String str) {
        char[] loweredStr = str.toLowerCase(Locale.ROOT).toCharArray();
        int countAs = 0;
        int countEs = 0;
        int countIs = 0;
        int countOs = 0;
        int countUs = 0;
        for (char c : loweredStr) {
            if (c == 'a') {
                countAs += 1;
            }
            if (c == 'e') {
                countEs += 1;
            }
            if (c == 'i') {
                countIs += 1;
            }
            if (c == 'o') {
                countOs += 1;
            }
            if (c == 'u') {
                countUs += 1;
            }
        }
        System.out.println("a: " + countAs + ", e: " + countEs + " ,i: " + countIs + " ,o: " + countOs + " ,u: " + countUs);
    }
}
