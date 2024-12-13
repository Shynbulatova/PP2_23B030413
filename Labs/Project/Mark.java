package Project;

public class Mark {
    private String courseName;
    private String markForCourse;

    public Mark(String courseName, String markForCourse) {
        this.courseName = courseName;
        this.markForCourse = markForCourse;
    }

    public String getCourseName() {
        return courseName;
    }

    public String getMarkForCourse() {
        return markForCourse;
    }

    @Override
    public String toString() {
        return "Mark{" +
                "courseName='" + courseName + '\'' +
                ", markForCourse='" + markForCourse + '\'' +
                '}';
    }
}
