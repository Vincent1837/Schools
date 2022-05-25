package stu_110502567;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import java.io.*;
import java.nio.charset.StandardCharsets;

public class A12_1_110502567 {
    public static void main(String[] args) {
        final String URL = "https://www.csie.ncu.edu.tw/";
        try{
            Document HTML = Jsoup.connect(URL).get();
            Document document = Jsoup.parse(String.valueOf(HTML)); //從URL加載文檔，使用Jsoup.connect()方法從URL加載HTML。
            File file = new File("A12_1_110502567.txt");
            OutputStream os = new FileOutputStream(file);
            os.write(String.valueOf(HTML).getBytes(StandardCharsets.UTF_8));
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
    }
}
