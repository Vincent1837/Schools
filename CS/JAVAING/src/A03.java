import java.util.ArrayList;
import java.util.Scanner;

/*
Assignment 03
Name: 你的姓名
Student Number: 你的學號
Course 2024-課程代碼-你的班級
*/
public class A03 {

    public static void main(String[] args) {

        // get user input
        Scanner s = new Scanner(System.in);
        int n, m;
        n = s.nextInt();
        m = s.nextInt();
        // get hacker
        int[] hacker = new int[n];
        for (int i = 0; i < n; i++) {
            hacker[i] = s.nextInt();
        }

        //get domain
        ArrayList<int[]> domain = new ArrayList<>(n);
        for (int i = 0; i < m; i++) {
            int[] row = new int[n];
            for (int j = 0; j < n; j++) {
                row[j] = s.nextInt();
            }
            domain.add(row);
        }

        //get method
        String method = s.next();

        System.out.println();
        System.out.println("n, m = " + n + m);
        System.out.print("hacker = ");
        for (int i = 0; i < n; i++) {
            System.out.print(hacker[i] + " ");
        }
        System.out.println();
        printDomain(domain);
        System.out.println("method = " + method);
    }

    public static int hacking_data_A (ArrayList<int[]> original_domain, int[] hacker) {
        int count = 0;
        for (int i = 0; i < original_domain.size(); i++) {
            original_domain.add(i, hacker);


            original_domain.remove(i);
        }

        return count;
    }

    public static int hacking_data_B (ArrayList<int[]> original_domain, int[] hacker) {
        return 0;
    }

    public static void printDomain (ArrayList<int[]> domain) {
        for (int[] l : domain) {
            for (int i : l) {
                System.out.print(l[i] + " ");
            }
            System.out.println();
        }
    }

}