/**
 * Practice 10
 * Student Number: 110502567
 * Course: 2022-CE1004-B
 */

package P10_110502567;

import java.util.ArrayList;
import java.util.Scanner;

public class P10_110502567 {
    public static void main(String[] args) {
        ArrayList<Integer> drinkOrdered = new ArrayList<>(0);
        int[] drinkAmount = {0, 0, 0, 0};
        String[] drinks = {"Cola", "Green Tea", "Lemon Tea", "Mineral Water"};
        int total = 0;
        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("(1)choose drinks (2)list (3)pay (4)exit");
            String input = sc.next();
            if (input.equals("1")) {
                System.out.println("choose drinks (drinks / amount)");
                System.out.println("(1)Cola (2)Green Tea (3)Lemon Tea (4)Mineral Water");
                int choice = sc.nextInt();
                int amount = sc.nextInt();
                if (choice == 1) {
                    drinkAmount[0] += amount;
                    if (drinkOrdered.contains(0)) {
                        total += 30 * amount;
                    } else {
                        drinkOrdered.add(0);
                        total += 30 * amount;
                    }
                } else if (choice == 2) {
                    drinkAmount[1] += amount;
                    if (drinkOrdered.contains(1)) {
                        total += 25 * amount;
                    } else {
                        drinkOrdered.add(1);
                        total += 25 * amount;
                    }
                } else if (choice == 3) {
                    drinkAmount[2] += amount;
                    if (drinkOrdered.contains(2)) {
                        total += 29 * amount;
                    } else {
                        drinkOrdered.add(2);
                        total += 29 * amount;
                    }
                } else if (choice == 4) {
                    drinkAmount[3] += amount;
                    if (drinkOrdered.contains(3)) {
                        total += 20 * amount;
                    } else {
                        drinkOrdered.add(3);
                        total += 20 * amount;
                    }
                } else {
                    System.out.println("invalid input");
                }
            } else if (input.equals("2")) {
                if (drinkOrdered.isEmpty()) {
                    System.out.println("Empty");
                } else {
                    for (int i : drinkOrdered) {
                        System.out.println(drinks[i] + ' ' + drinkAmount[i]);
                    }
                }
            } else if (input.equals("3")) {
                System.out.println("total cost: " + total);
                System.out.println("please pay");
                int paid = sc.nextInt();
                if (paid >= total) {
                    System.out.println("money change: " + (paid - total));
                    System.out.println("thank you");
                    break;
                } else {
                    System.out.println("money not enough");
                }
            } else if (input.equals("4")) {
                System.out.println("exit");
                break;
            } else {
                System.out.println("invalid input");
            }
        }
    }
}
