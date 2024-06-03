public class ExamResult {
    private String courseName;
    private int score;

    public ExamResult(String courseName, int score) {
        this.courseName = courseName;
        this.score = score;
    }
    
    public void displayResult() {
        System.out.println("Course: " + courseName);
        System.out.println("Score: " + score);
    }
}
