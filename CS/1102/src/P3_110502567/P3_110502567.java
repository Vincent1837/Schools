package P3_110502567;
/*
Practice 3
Student Number: 110502567
Course: 2022-CE1004-B
*/
class Student {
    // do something here
    Student(String NAME, int SCORE){
        this.NAME = NAME;
        this.SCORE = SCORE;
    }
    private String NAME;
    private int SCORE;

    public String getName(){
        return NAME;
    }
    public int getScore(){
        return SCORE;
    }
    public void changeScore(int new_score){
        SCORE = new_score;
    }
}

public class P3_110502567 {
    public static void main(String[] args) {
        // 以下不要改
        Student putin = new Student("Putin", 59);
        System.out.println(putin.getName() + " before: " + putin.getScore());
        putin.changeScore(40);
        System.out.println(putin.getName() + " after: " + putin.getScore());
//        putin.score = 100;
    }
}