package P12_110502567;

import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class P12_110502567 {

    public static void main(String[] args) throws IOException {
        double[][] points = {{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}};
        double[][] circles = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        double[] line = {0, 0, 0};

        File file = new File("m2-2.txt");
        Scanner input = new Scanner(file);

        String currLine = input.nextLine();
        currLine = currLine.replaceAll("\\[", "");
        currLine = currLine.replaceAll("]", "");
        currLine = currLine.replaceAll(",", " ");
        Scanner scanPoints = new Scanner(currLine);

        for(int i = 0; i < 5; ++i) {

            points[i][0] = scanPoints.nextInt();

            points[i][1] = scanPoints.nextInt();

        }

        currLine = input.nextLine();
        currLine =  currLine.replaceAll("\\[", "");
        currLine = currLine.replaceAll("]", "");
        currLine = currLine.replaceAll(",", " ");
        Scanner scanCircle = new Scanner(currLine);
        for(int i = 0; i < 4; ++i) {

            circles[i][0] = scanCircle.nextInt();

            circles[i][1] = scanCircle.nextInt();

            circles[i][2] = scanCircle.nextInt();

        }

        currLine = input.nextLine();
        currLine = currLine.replaceAll("\\[", "");
        currLine = currLine.replaceAll("]", "");
        currLine = currLine.replaceAll(",", " ");
        Scanner scanLines = new Scanner(currLine);
        line[0] = scanLines.nextInt();
        line[1] = scanLines.nextInt();
        line[2] = scanLines.nextInt();

        for(int i = 0; i < 4; ++i) {
            int num = 0;
            for(int j = 0; j < 5; ++j) {
                if(Math.pow(circles[i][0] - points[j][0], 2) + Math.pow(circles[i][1] - points[j][1], 2) <= Math.pow(circles[i][2], 2)) {
                    ++num;
                }
            }
            System.out.print(Integer.toString(num) + ' ');
        }

        for(int i = 0; i < 4; ++i) {
            double distance = (Math.abs(line[0] * circles[i][0] + line[1] * circles[i][1] + line[2])) / Math.pow(Math.pow(line[0], 2) + Math.pow(line[1], 2), 0.5);
            if(distance == circles[i][2]) {
                System.out.print("tangency" + ' ');
            }else if(distance > circles[i][2]) {
                System.out.print("disjoint" + ' ');
            }else if(distance < circles[i][2]) {
                System.out.print("intersect" + ' ');
            }
        }

        System.out.println("");
        input.close();
        scanPoints.close();
        scanLines.close();
        scanCircle.close();
    }

}