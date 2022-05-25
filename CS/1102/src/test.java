import java.util.Scanner;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileNotFoundException;

public class test {
    public static void main(String[] args) {
        A a1 = new A();
        a1.i = 12;
        a1.j = 4;

        A a2 = new A(5, 23);

        B b = new B();
        b.k = 123;

        a1.printij();
        a2.printij();
        b.j = 4;
        b.printijk();

    }
}

class A {
    public A(){}

    public A (int i, int j) {
        this.i = i;
        this.j = j;
    }

    int i, j;

    public void printij() {
        System.out.println(" " + i + j);
    }
}

class B extends A {
    public B() {}

    public B(int i, int j) {
        super(i, j);
        //TODO Auto-generated constructor stub
    }

    int k ;

    public void printijk() {
        System.out.println(i+j+k);
    }
}
