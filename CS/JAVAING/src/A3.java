import org.w3c.dom.ls.LSInput;

import java.util.ArrayList;
import java.util.*;

public class A3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            int input = sc.nextInt();
            if (input == -1){
                break;
            }
            for (int i : findFactors(input)){
                System.out.println(i + " " + isPrime(i));
            }
        }

    }
    private static ArrayList<Integer> findFactors(int num){
        ArrayList<Integer> factors = new ArrayList<>();
        for (int i = 1; i < Math.sqrt(num); i++){
            if (num % i == 0){
                factors.add(i);
                factors.add(num / i);
            }
            Collections.sort(factors);
        }
        return factors;
    }
    private static String isPrime(int num){
        if (num == 1){
            return "False";
        }
        boolean flag = true;
        for (int i = 2; i < Math.sqrt(num); i++){
            if (num % i == 0){
                flag = false;
            }
        }
        return flag ? "True" : "False";
    }
}
