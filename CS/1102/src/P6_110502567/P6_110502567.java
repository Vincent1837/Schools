/**
 * Practice 5
 * Student Number: 110502567
 * Course: 2022-CE1004-B
 */
package P6_110502567;

import java.util.ArrayList;
import java.util.Scanner;

public class P6_110502567 {
    public static void main(String[] args) {
        String[] bookshelf = new String[10];
        Scanner sc = new Scanner(System.in);

        while (true) {
            String input = sc.nextLine();
            if (input.equals("exit")) {
                break;
            } else if (input.charAt(0) == '1') {
                if (bookshelf[input.charAt(2) - 49] != null) {
                    String[] temp = new String[11];
                    for (int i = input.charAt(2) - 49; i < 10; i++) {
                        temp[i+1] = bookshelf[i];
                    }
                    bookshelf[input.charAt(2) - 49] = input.substring(4);
                    for (int i = input.charAt(2) - 48; i < 10; i++) {
                        bookshelf[i] = temp[i];
                    }
                } else {
                    bookshelf[input.charAt(2) - 49] = input.substring(4);
                }
            } else if (input.charAt(0) == '2') {
                bookshelf[input.charAt(2) - 49] = null;
            }

            // sort the bookshelf
            String[] temp = new String[10];
            int count = 0;
            for (int i = 0; i < 10; i++) {
                if (bookshelf[i] != null) {
                    temp[count] = bookshelf[i];
                    count += 1;
                }
            }
            for (int i = 0; i < 10; i++) {
                bookshelf[i] = null;
            }
            System.arraycopy(temp, 0, bookshelf, 0, 10);
        }
        // print the bookshelf ArrayList
        ArrayList<String> sortedBookShelf = new ArrayList<>();
        for (String book : bookshelf) {
            if (book != null) {
                sortedBookShelf.add(book);
            }
        }
        sc.close();
        System.out.print(sortedBookShelf);
    }
}
