import java.util.ArrayList;

public class Student {
    private String name;
    private ArrayList<ExamResult> examResults;

    public Student(String name) {
        this.name = name;
        this.examResults = new ArrayList<>();
    }

    public void addExamResult(ExamResult examResult) {
        examResults.add(examResult);
    }

    public void displayExamResults() {
        System.out.println("Student: " + name);
        for (ExamResult examResult : examResults) {
            examResult.displayResult();
        }
    }
}