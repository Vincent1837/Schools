/**
 * Assignment 10
 * Student Number: 110502567
 * Course: CE_1002
 */
package A10_110502567;
import java.util.InputMismatchException;
import java.util.Scanner;

public class A10_110502567_1 {
    public static void main(String[] args) {
        while (true) {
            System.out.println("請輸入整數");
            Scanner sc = new Scanner(System.in);
            try {
                int a = sc.nextInt();
                int b = sc.nextInt();
                if (a < 0 || b < 0) {
                    throw new IllegalArgumentException();
                }
                System.out.println(a / b);
                break;
            } catch (ArithmeticException ex) {
                System.out.println("分母不能為零");
                sc.nextLine();
            } catch (InputMismatchException ex) {
                System.out.println("輸入為非整數");
                sc.nextLine();
            } catch (IllegalArgumentException ex) {
                System.out.println("分子或分母為負數了!");
                sc.nextLine();
            }
        }
    }
}
