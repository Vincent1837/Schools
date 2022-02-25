package P2_110502567;
/*
Practice 2
Student Number: 110502567
Course: 2022-CE1004-B
*/
import java.io.*;
import java.util.Scanner;

public class P2_110502567{
    public static void main(String[] args){
        try {
            File testFile = new File("test.txt");
            File newFile = new File("110502567.txt");
            if (newFile.createNewFile()){
                System.out.println(newFile.getName() + " created.");
            } else {
                System.out.println("File already existed.");
            }
            FileWriter writer = new FileWriter(newFile);
            Scanner sc = new Scanner(testFile);
            while (sc.hasNextLine()){
                String content = sc.nextLine();
                writer.write(content + "\n");
                writer.flush();
            }
            writer.close();
            sc.close();
        } catch (IOException ex) {
            System.out.println("An error occurred.");
            ex.printStackTrace();
        }
    }
}
