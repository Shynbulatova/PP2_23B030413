package Project;

public class Transcript {
    private String courseName;
    private Mark mark;

    public Transcript(String courseName, Mark mark) {
        this.courseName = courseName;
        this.mark = mark;
    }

    public String getCourseName() {
        return courseName;
    }

    public Mark getMark() {
        return mark;
    }

    public boolean has70Mark() {
        try {
            double markValue = Double.parseDouble(mark.getMarkForCourse());
            return markValue >= 70.0;
        } catch (NumberFormatException e) {
            return false; 
        }
    }

    @Override
    public String toString() {
        return "Transcript{" +
                "courseName='" + courseName + '\'' +
                ", mark=" + mark +
                '}';
    }
}

