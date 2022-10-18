/**
* Practice 4
* Student Number: 110502567
* Course: 2022-CE1004-B
*/
package P4_110502567;

class Pet {
    public void speak(){
        System.out.println("Pet speaking");
    }
}

class Cat extends Pet {
    public void speak(){
        System.out.println("Cat speaking");
    }
}

class Dog extends Pet {
    public void speak(){
        System.out.println("Dog speaking");
    }
}

class  newborn_Cat extends Cat {
    public void speak(){
        System.out.println("Meow");
    }
}

class  newborn_Dog extends Dog {
    public void speak(){
        System.out.println("Woof");
    }
}

public class P4_110502567 {
    public static void main(String[] args) {
        // 以下不要改
        Pet putin = new Pet();
		Cat neko  = new Cat();
		Dog inu   = new Dog();
		newborn_Cat meow = new newborn_Cat();
		newborn_Dog woof = new newborn_Dog();
		putin.speak();
		neko.speak();
		inu.speak();
		meow.speak();
		woof.speak();
    }
}