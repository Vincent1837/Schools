/**
 * Practice 5
 * Student Number: 110502567
 * Course: 2022-CE1004-B
 */
package P5_110502567;

import java.util.Scanner;

public class P5_110502567 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please Create a hero:");
        System.out.print("Name: ");
        String heroName = sc.next();

        System.out.print("Hp: ");
        int heroHp = sc.nextInt();

        System.out.print("Atk: ");
        int heroAtk = sc.nextInt();

        System.out.printf("%s's Weapon: ", heroName);
        String heroWeapon = sc.next();

        System.out.printf("%s Weapon Atk: ", heroName);
        int heroWeaponAtk = sc.nextInt();

        System.out.println();
        Hero hero = new Hero(heroName, heroHp, heroAtk, heroWeapon, heroWeaponAtk);

        while (true) {
            System.out.println("Please Create a enemy:");
            System.out.print("Name: ");
            String enemyName = sc.next();

            System.out.print("Hp: ");
            int enemyHp = sc.nextInt();

            System.out.print("Atk: ");
            int enemyAtk = sc.nextInt();

            System.out.print("DropItem: ");
            String enemyDropItem = sc.next();

            Enemy enemy = new Enemy(enemyName, enemyHp, enemyAtk, enemyDropItem);
            boolean enemyDied = false;
            boolean heroDied = false;
            System.out.println("============");

            System.out.printf("A Wild %s appeared!\n", enemyName);
            System.out.printf("What will %s do?\n", enemyName);
            while (true) {
                System.out.printf("%s's Hp: %s\n", hero.NAME, hero.HP);
                System.out.printf("%s's Hp: %s\n", enemy.NAME, enemy.HP);
                System.out.println("1.Attack 2.Do nothing.");
                if (sc.nextInt() == 1) {
                    System.out.printf("%s use %s and hurt %s %d points.\n", hero.NAME, hero.WEAPON, enemy.NAME, hero.ATK + hero.WEAPONATK);
                    enemy.HP -= hero.ATK + hero.WEAPONATK;
                } else {
                    System.out.printf("%s is doing nothing\n", hero.NAME);
                }
                if (enemy.HP <= 0) {
                    enemyDied = true;
                    break;
                }
                hero.HP -= enemyAtk;
                if (hero.HP <= 0) {
                    heroDied = true;
                    break;
                }
            }
            if (enemyDied) {
                System.out.printf("%s win!\n", hero.NAME);
                System.out.printf("%s dropped item %s left on the ground.\n", enemy.NAME, enemy.DROPITEM);
                System.out.println("Want another adventure?");
                System.out.println("1. Yes 2. No");
                if (sc.nextInt() == 2) {
                    System.out.println("Game Over");
                    break;
                }
            }
            if (heroDied) {
                System.out.printf("%s win!\n", enemy.NAME);
                System.out.printf("%s's weapon %s left on the ground.\n", hero.NAME, hero.WEAPON);
                System.out.println("Game Over");
                break;
            }
        }

        sc.close();
    }
}

class Role{
    String NAME;
    int HP, ATK;
}

class Hero extends Role{
    String WEAPON;
    int WEAPONATK;

    public Hero(String NAME, int HP, int ATK, String WEAPON, int WEAPONATK){
        this.NAME = NAME;
        this.HP = HP;
        this.ATK = ATK;
        this.WEAPON = WEAPON;
        this.WEAPONATK = WEAPONATK;
    }
}

class Enemy extends Role{
    String DROPITEM;

    public Enemy(String NAME, int HP, int ATK, String DROPITEM){
        this.NAME = NAME;
        this.HP = HP;
        this.ATK = ATK;
        this.DROPITEM = DROPITEM;
    }
}