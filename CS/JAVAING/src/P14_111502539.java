import java.util.Scanner;

public class P14_111502539 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double num1, num2, result;
        String operator;

        try {
            System.out.print("Enter the first number: ");
            num1 = readNumber(scanner);

            System.out.print("Enter the operator (+, -, *, or /): ");
            operator = readOperator(scanner);

            System.out.print("Enter the second number: ");
            num2 = readNumber(scanner);

            result = calculateResult(num1, num2, operator);
            System.out.println("Result: " + roundToDecimal(result, 1));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    private static double readNumber(Scanner scanner) throws Exception {
        if (scanner.hasNextDouble()) {
            double number = scanner.nextDouble();
            if (number >= -100.0 && number <= 100.0) {
                return number;
            }
        }
        throw new Exception("Invalid number! Please enter again: ");
    }

    private static String readOperator(Scanner scanner) throws Exception {
        String operator = scanner.next();
        if (operator.equals("+") || operator.equals("-") || operator.equals("*") || operator.equals("/")) {
            return operator;
        }
        throw new Exception("Invalid operator! Please enter again: ");
    }

    private static double calculateResult(double num1, double num2, String operator) throws Exception {
        switch (operator) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                if (num2 != 0) {
                    return num1 / num2;
                } else {
                    throw new Exception("Divisor cannot be zero!\n");
                }
        }
        throw new Exception("Invalid operator! Please enter again: ");
    }

    private static double roundToDecimal(double number, int decimalPlaces) {
        double powerOfTen = Math.pow(10, decimalPlaces);
        return Math.round(number * powerOfTen) / powerOfTen;
    }
}
