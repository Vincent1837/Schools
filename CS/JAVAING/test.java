import java.util.Scanner;

public class test {
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
        } catch (InvalidNumberException | InvalidOperatorException | DivisionByZeroException e) {
            System.out.println(e.getMessage());
        }
    }

    private static double readNumber(Scanner scanner) throws InvalidNumberException {
        if (scanner.hasNextDouble()) {
            double number = scanner.nextDouble();
            if (number >= -100.0 && number <= 100.0) {
                return number;
            }
        }
        throw new InvalidNumberException("Invalid number! Please enter again: ");
    }

    private static String readOperator(Scanner scanner) throws InvalidOperatorException {
        String operator = scanner.next();
        if (operator.equals("+") || operator.equals("-") || operator.equals("*") || operator.equals("/")) {
            return operator;
        }
        throw new InvalidOperatorException("Invalid operator! Please enter again: ");
    }

    private static double calculateResult(double num1, double num2, String operator) throws DivisionByZeroException, InvalidOperatorException {
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
                    throw new DivisionByZeroException("Divisor cannot be zero!\n");
                }
        }
        throw new InvalidOperatorException("Invalid operator! Please enter again: ");
    }

    private static double roundToDecimal(double number, int decimalPlaces) {
        double powerOfTen = Math.pow(10, decimalPlaces);
        return Math.round(number * powerOfTen) / powerOfTen;
    }
}

class InvalidNumberException extends Exception {
    public InvalidNumberException(String message) {
        super(message);
    }
}

class InvalidOperatorException extends Exception {
    public InvalidOperatorException(String message) {
        super(message);
    }
}

class DivisionByZeroException extends Exception {
    public DivisionByZeroException(String message) {
        super(message);
    }
}
