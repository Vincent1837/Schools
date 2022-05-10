package stu_110502567;

import java.util.ArrayList;
import java.util.Scanner;

public class E1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        record item (int id, String name, int price, int amount) {}
        ArrayList<item> cart = new ArrayList<>();
        while (true) {
            System.out.println("選擇一個指令 :\n添加商品 : add\n查詢購物車商品 : query\n修改商品數量 : update\n結算金額 : pay");
            String action = sc.next();
            if (action.equals("add")) {
                System.out.println("請輸入入商品編號 :");
                int id = sc.nextInt();
                System.out.println("請輸入入商品名稱 :");
                String name = sc.next();
                System.out.println("請輸入入商品價格 :");
                int price = sc.nextInt();
                System.out.println("請輸入入商品數量 :");
                int amount = sc.nextInt();
                cart.add(new item(id, name, price, amount));
                System.out.println("您的商品" + name + "已添加到購物車");
            } else if (action.equals("query")) {
                System.out.println("=======================購物車內容如下=======================");
                System.out.printf("%-9s%-14s%-9s%-10s\n", "編號", "名稱", "價格", "數量");
                for (int i = 0; i < cart.size(); i++) {
                    System.out.printf("%-10s%-16s%-10s%-10s\n", cart.get(i).id(), cart.get(i).name, cart.get(i).price, cart.get(i).amount);
                }
            } else if (action.equals("update")) {
                System.out.println("請輸入需要修改的商品編號: ");
                int editId = sc.nextInt();
                boolean flag = false;
                int index = 0;
                for (item i : cart) {
                    if (i.id == editId) {
                        flag = true;
                    } else {
                        index++;
                    }
                }
                if (flag) {
                    System.out.println("請輸入商品" + cart.get(index).name + "的修改數量");
                    int editAmount = sc.nextInt();
                    cart.set(index, new item(cart.get(index).id, cart.get(index).name, cart.get(index).price, editAmount));
                    System.out.println("修改完成");
                    System.out.println("=======================購物車內容如下=======================");
                    System.out.printf("%-9s%-14s%-9s%-10s\n", "編號", "名稱", "價格", "數量");
                    for (int i = 0; i < cart.size(); i++) {
                        System.out.printf("%-10s%-16s%-10s%-10s\n", cart.get(i).id(), cart.get(i).name, cart.get(i).price, cart.get(i).amount);
                    }
                } else {
                    System.out.println("無此商品");
                }
            } else if (action.equals("pay")) {
                double pay = 0;
                System.out.println("=======================購物車內容如下=======================");
                System.out.printf("%-9s%-14s%-9s%-10s\n", "編號", "名稱", "價格", "數量");
                for (int i = 0; i < cart.size(); i++) {
                    pay += cart.get(i).price * cart.get(i).amount;
                    System.out.printf("%-10s%-16s%-10s%-10s\n", cart.get(i).id(), cart.get(i).name, cart.get(i).price, cart.get(i).amount);
                }
                System.out.println("訂單總金額: " + pay);
            } else if (action.equals("exit")) {
                break;
            } else {
                System.out.println("沒有改功能");
            }
        }
        sc.close();
    }

}
