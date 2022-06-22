package stu_110502567;

import java.util.Scanner;

public class E1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String date1;
        String date2;
        //main
        while(true){
            date1 = input.nextLine();
            if(date1.equals("0"))
                break;
            date2 = input.nextLine();
            //format
            date1 = date1.replaceAll(",","");
            date2 = date2.replaceAll(",","");
            String[] formatDate1 = date1.split(" ");
            String[] formatDate2 = date2.split(" ");
            //cal ans
            int ans = 0;
            for(int i = Integer.parseInt(formatDate1[2]) ; i<=Integer.parseInt(formatDate2[2]) ; i++){
                if(Math.abs(i)%4 == 0)
                    ans++;
                if(Math.abs(i)%100 == 0)
                    ans--;
                if(Math.abs(i)%400 == 0)
                    ans++;
            }
            //process front and end
            if(Math.abs(Integer.parseInt(formatDate1[2]))%4 == 0){
                if(Math.abs(Integer.parseInt(formatDate1[2]))%100 == 0 && Math.abs(Integer.parseInt(formatDate1[2]))%400 != 0){
                    break;
                }
                if(!(formatDate1[0].equals("January")) && !(formatDate1[0].equals("February")&&Integer.parseInt(formatDate1[1])<=29)){
                    ans--;
                }
            }
            if(Math.abs(Integer.parseInt(formatDate2[2]))%4 == 0){
                if(Math.abs(Integer.parseInt(formatDate2[2]))%100 == 0 && Math.abs(Integer.parseInt(formatDate2[2]))%400 != 0){
                    break;
                }
                if(formatDate2[0].equals("January") || (formatDate2[0].equals("February") && Integer.parseInt(formatDate2[1])<=28)){
                    ans--;
                }
            }
            System.out.println(ans);
        }
    }
}
