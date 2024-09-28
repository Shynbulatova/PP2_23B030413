package Labs;
//4
import java.util.ArrayList;
import java.util.Scanner;

public class GradeBook {
    private String courseName;
    private ArrayList<Integer> grades;

    public GradeBook(String courseName) {
        this.courseName = courseName;
        grades = new ArrayList<>();
    }

    public void addGrade(int grade) {
        grades.add(grade);
    }

    public double getAverage() {
        if (grades.isEmpty()) return 0;
        int sum = 0;
        for (int grade : grades) {
            sum += grade;
        }
        return (double) sum / grades.size();
    }

    public void displayGradeReport() {
        System.out.println("Class average is " + getAverage());
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        GradeBook gradeBook = new GradeBook("CS101");

        System.out.println("Please enter grades (Q to quit):");
        while (input.hasNextInt()) {
            int grade = input.nextInt();
            gradeBook.addGrade(grade);
        }

        gradeBook.displayGradeReport();
    }
}

