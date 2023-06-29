
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class BaseCar {
    protected String driver;
    protected int speed;
    protected int driver_boost;
    protected int carboost;
    protected int currentSpeed;
    protected int currentPosition;
    protected boolean isWinner;
    protected boolean isBoosting;

    public BaseCar(String driver, int speed, int driver_boost, int carboost) {
        this.driver = driver;
        this.speed = speed;
        this.driver_boost = driver_boost;
        this.carboost = carboost;
        this.currentSpeed = speed + driver_boost;
        this.currentPosition = 0;
        this.isWinner = false;
        this.isBoosting = false;
    }

    public int getCurrentSpeed(int second) {
        return speed + carboost * second + driver_boost * second;  //
    }

    public String getDriver() {
        return driver;
    }
}

class Benz extends BaseCar {
    public Benz(String driver, int speed, int driver_boost, int carboost) {
        super(driver, speed, driver_boost,carboost);
    }
}

class BMW extends BaseCar {
    public BMW(String driver, int speed, int driver_boost, int carboost) {
        super(driver, speed, driver_boost,carboost);
    }
}

class Mazda extends BaseCar {
    public Mazda(String driver, int speed, int driver_boost, int carboost) {
        super(driver, speed, driver_boost,carboost);
    }
}

public class A13_111502539 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int lane = scanner.nextInt();
        int numDrivers = scanner.nextInt();
        scanner.nextLine();

        List<BaseCar> carList = new ArrayList<>();
        for (int i = 0; i < numDrivers; i++) {
            String[] input = scanner.nextLine().split(" ");
            String driver = input[0];
            int carType = Integer.parseInt(input[1]);

            BaseCar car;
            if (carType == 1) {
                car = new Benz(driver, 14, getDriverBoost(driver),5);
            } else if (carType == 2) {
                car = new BMW(driver, 8, getDriverBoost(driver),8);
            } else {
                car = new Mazda(driver, 11, getDriverBoost(driver),2);
            }

            carList.add(car);
        }
        scanner.close();
        
        // race loop
        for (int second = 0; second < 560; second++) {

            // check game over
        	boolean gameover = false;
        	int winnersCount = 0;
        	for (BaseCar car : carList) {
        		if (car.currentPosition >= lane) {
        			car.isWinner = true;
        			winnersCount += 1;
        			gameover = true;
        		}
        	}
        	if (gameover) {
                if (winnersCount > 1) {
                    System.out.print("More that 1 winner!");
                    printPositions(carList);
                    break;
                } else {
                    for (BaseCar car : carList) {
                        if (car.isWinner) {
                            System.out.print(car.driver + " wins!");
                            printPositions(carList);
                        }
                    }
                    break;
                }
        	}
        	
            // in every 10 sec
            if (second % 10 == 0 && second != 0) {
                System.out.print("When " + second + "sec starts,");
                printPositions(carList);
                // find the last place and boost it
                for (BaseCar car : carList) {
                    car.isBoosting = false;
                }
                int lastOne = 6000;
                for (BaseCar car : carList) {
                    if (car.currentPosition < lastOne) {
                        lastOne = car.currentPosition;
                    }
                }
                for (BaseCar car : carList) {
                    if (car.currentPosition == lastOne) {
                        car.isBoosting = true;
                    }
                }
            }
            
            // make the cars run
            for (BaseCar car : carList) {
                car.currentPosition += car.currentSpeed;
                if (car.isBoosting) {
                    car.currentPosition += car.carboost;
                }
            }


        }
    }

    private static int getDriverBoost(String driver) {
        switch (driver) {
            case "A":
                return 3;
            case "B":
                return 2;
            case "C":
                return 1;
            case "D":
                return 3;
            case "E":
                return 10;
            case "F":
                return 2;
            case "G":
                return 1;
            default:
                return 0;
        }
    }

    private static void printPositions (List<BaseCar> carList) {
    	for (BaseCar car : carList) {
            System.out.print(' ' + car.driver + ':' + car.currentPosition + 'm');
        }
        System.out.println();
    }	
}