/**
 * Assignment 4
 * Student Number: 110502567
 * Course: CE_1002
 */
package A4_110502567;

class Character {
    Character(String name, int level, int health) {
        this.name =  name;
        this.level = level;
        this.health = health;
    }

    private String name;

    private int level;

    private int health;

    public String getName(){
        return name;
    }

    public int getLevel(){
        return level;
    }

    public int getHealth(){
        return health;
    }
}
class Archer extends Character {
    Archer(String name, int level, int health) {
        super(name, level, health);
    }

    public void Attack(){
        System.out.println("弓箭手 : 發射弓箭");
    }

    public void Reload(){
        System.out.println("弓箭手 : 填裝彈藥");
    }
}
class Medic extends Character {
    Medic(String name, int level, int health) {
        super(name, level, health);
    }

    public void Cure(){
        System.out.println("醫護兵 : 治癒中");
    }
}

public class A4_110502567 {
    static public void main(String[] args){
        Archer archer = new Archer("Alex",10,100);
        Medic medic = new Medic("Justin",5,100);
        System.out.printf("弓箭手：(%s, %d, %d)%n", archer.getName(),archer.getLevel(), archer.getHealth());
        System.out.printf("醫護兵：(%s, %d, %d)%n", medic.getName(),medic.getLevel(), medic.getHealth());
        archer.Reload();
        archer.Attack();
        medic.Cure();
    }
}