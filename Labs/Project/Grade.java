package Project;

public class Grade {
    private double firstAtt;
    private double secondAtt;
    private double finalMark;

    public Grade(double firstAtt, double secondAtt, double finalMark) {
        this.firstAtt = firstAtt;
        this.secondAtt = secondAtt;
        this.finalMark = finalMark;
    }

    public double getFirstAtt() {
        return firstAtt;
    }

    public double getSecondAtt() {
        return secondAtt;
    }

    public double getFinalMark() {
        return finalMark;
    }

    @Override
    public String toString() {
        return "Grade{" +
                "firstAtt=" + firstAtt +
                ", secondAtt=" + secondAtt +
                ", finalMark=" + finalMark +
                '}';
    }
}
