package stu_110502567.stu_110502531;

import java.util.Scanner;

public class E2 {
    static char [][] map;
    static char [][] temp;
    static int m, n;
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        while(true) {
            m = input.nextInt();
            if(m == 0) break;
            n = input.nextInt();
            int k = input.nextInt();

            map = new char[m][n];
            temp = new char[m][n];
            input.nextLine();

            for (int i = 0; i < m; ++i) {
                String line = input.nextLine();
                for (int j = 0; j < n; ++j) {
                    map[i][j] = line.charAt(j);
                    temp[i][j] = line.charAt(j);
                }
            }

            for(int a = 0; a < k; ++a) {
                for (int i = 0; i < m; ++i) {
                    for (int j = 0; j < n; ++j) {
                        if (map[i][j] == '1') {
                            if (count(i, j) != 2 && count(i, j) != 3) {
                                temp[i][j] = '0';
                            }
                        } else {
                            if (count(i, j) == 3) {
                                temp[i][j] = '1';
                            }
                        }
                    }
                }

                for (int i = 0; i < m; ++i) {
                    for (int j = 0; j < n; ++j) {
                        map[i][j] = temp[i][j];
                    }
                }
            }

            for (int i = 0; i < m; ++i) {
                for (int j = 0; j < n; ++j) {
                    System.out.print(temp[i][j]);
                }
                System.out.print('\n');
            }

        }
    }

    public static int count(int i, int j) {
        int num = 0;
        int rowStart = i - 1;
        int columnStart = j - 1;
        for(int x = rowStart; x < rowStart + 3; ++x) {
            for(int y= columnStart; y < columnStart + 3; ++y) {
                if(x == i && y == j) continue;
                if((x >= 0 && x < m) && (y >= 0 && y < n)) {
                  if(map[x][y] == '1') ++num;
                }
            }
        }
        return num;
    }
}