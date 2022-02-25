/*
Assignment 2
Student Number: 110502567
Course: CE_1002
*/
import java.util.Scanner;
class A2_110502567 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int height = sc.nextInt();
        // System.out.println(height);
        String string = sc.next();
        for (int i = 0; i < height-1; i++){
            for (int j = 0; j < height-1-i; j++){
                System.out.print(' ');
            }
            System.out.print(string.charAt(0));
            for (int j = 0; j < i*2; j++){
                System.out.print(string.charAt(1));
            }
            System.out.print(string.charAt(0));
            for (int j = 0; j < 4-i; j++){
                System.out.print(' ');
            }
            System.out.println();
        }
        for (int i = 0; i < height*2; i++){
            System.out.print(string.charAt(0));  
        }
        sc.close();
    }
}