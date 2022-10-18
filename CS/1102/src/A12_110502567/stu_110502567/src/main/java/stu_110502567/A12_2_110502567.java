package stu_110502567;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class line {
    String str = "";
    int year, month, day;

    public line(String str) {
        this.str = str;
        year = Integer.parseInt(str.substring(0, 4));
        month = Integer.parseInt(str.substring(5, 7));
        day = Integer.parseInt(str.substring(8, 10));
    }

    @Override
    public String toString() {
        return str;
    }
}

class yearCom implements Comparator<line> {
    @Override
    public int compare(line o1, line o2) {
        return -(o1.year - o2.year);
    }
}

class monthCom implements Comparator<line> {
    @Override
    public int compare(line o1, line o2) {
        return -(o1.month - o2.month);
    }
}

class dayCom implements Comparator<line> {
    @Override
    public int compare(line o1, line o2) {
        return -(o1.day - o2.day);
    }
}

public class A12_2_110502567 {
    public static void main(String[] arg) {
        try{
            ArrayList<line> lines = new ArrayList<line>();
            Document document = Jsoup.parse(new File("A12_1_110502567.txt"),"UTF-8");       //使用Jsoup.parse()方法從文件加載HTML。
            int length = document.select("div.item-title").size();//儲存我們所要的標籤的數量
            for(int i=0 ; i<length ; i++){
                lines.add(new line(document.select("div.item-time").get(i).text()+"    "+document.select("div.item-title").get(i).text()));
            }
            Collections.sort(lines, new dayCom());
            Collections.sort(lines, new monthCom());
            Collections.sort(lines, new yearCom());
            System.out.println(length);
            for(int i=0 ; i<length ; i++){
                System.out.println(lines.get(i).toString());;
            }
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }

    }
}