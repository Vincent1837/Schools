// please write Shape and Color here
interface Shape {
    double calculateArea();
    double calculatePerimeter();
}

interface Color {
    void setColor(String color);
    String getColor();
}

class Square implements Shape, Color /* extends or implents here */ {
    private double sideLength;
    private String color;
	
    // add any function here if you need
    public Square (double sideLength) {
        this.sideLength = sideLength;
    }

    @Override
    public double calculateArea() {
        return this.sideLength * this.sideLength;
    }
    
    @Override
    public double calculatePerimeter() {
        return this.sideLength * 4;
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String getColor() {
        return this.color;
    }
}

class Rectangle implements Shape, Color/* extends or implents here */ {
    private double length;
    private double width;
    private String color;

    // add any function here if you need
    public Rectangle (double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public double calculateArea() {
        return this.length * this.width;
    }
    
    @Override
    public double calculatePerimeter() {
        return (this.length + this.width) * 2;
    }

    @Override
    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String getColor() {
        return this.color;
    }
}

// please don't modify the testcases below

public class Main {
    public static void main(String[] args) {
        Square square = new Square(5);
        square.setColor("Red");
        System.out.println("Square Area: " + square.calculateArea());
        System.out.println("Square Perimeter: " + square.calculatePerimeter());
        System.out.println("Square Color: " + square.getColor());

        Rectangle rectangle = new Rectangle(3, 4);
        rectangle.setColor("Blue");
        System.out.println("Rectangle Area: " + rectangle.calculateArea());
        System.out.println("Rectangle Perimeter: " + rectangle.calculatePerimeter());
        System.out.println("Rectangle Color: " + rectangle.getColor());

        Shape shape = new Rectangle(7, 9);
        System.out.println("Shape Area: " + shape.calculateArea());
        System.out.println("Shape Perimeter: " + shape.calculatePerimeter());
        
        Color color = new Square(6);
        color.setColor("Green");
        System.out.println("Color: " + color.getColor());
    }
}
/*
Square Area: 25.0
Square Perimeter: 20.0
Square Color: Red
Rectangle Area: 12.0
Rectangle Perimeter: 14.0
Rectangle Color: Blue
Shape Area: 63.0
Shape Perimeter: 32.0
Color: Green
*/