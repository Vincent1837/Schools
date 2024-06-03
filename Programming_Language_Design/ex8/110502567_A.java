import java.lang.reflect.*;
// no need to import ExamResult and Student

public class PracticeA {
    public static void main(String[] args) {
        // ↓ Rewrite using Reflection ↓
        try {
            Class<?> studentClass = Class.forName("Student");
            Constructor<?> studentConstructor = studentClass.getConstructor(String.class);
            Object student = studentConstructor.newInstance("Alice");

            Class<?> examResultClass = Class.forName("ExamResult");
            Constructor<?> examResultConstructor = examResultClass.getConstructor(String.class, int.class);
            Object mathExamResult = examResultConstructor.newInstance("Math", 85);
            Object scienceExamResult = examResultConstructor.newInstance("Science", 90);

            Method addExamResultMethod = studentClass.getMethod("addExamResult", examResultClass);
            addExamResultMethod.invoke(student, mathExamResult);
            addExamResultMethod.invoke(student, scienceExamResult);

            Method displayExamResultsMethod = studentClass.getMethod("displayExamResults");
            displayExamResultsMethod.invoke(student);

        } catch (Exception e) {
            e.printStackTrace();
        }
        /* Student student = new Student("Alice");
        student.addExamResult(new ExamResult("Math", 85));
        student.addExamResult(new ExamResult("Science", 90));
        student.displayExamResults(); */
        // ↑ Rewrite using Reflection ↑
    }
}
/*
Student: Alice
Course: Math
Score: 85
Course: Science
Score: 90
*/