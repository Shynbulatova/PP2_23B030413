package task1;

public class Cube extends Shape3d {
    //S = 6a^2 V = a^3
    private double length;
    public Cube(double a) {
        this.length = a;


    }

    public double getLength() {
        return length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double volume() {
        return Math.pow(length, 3);
    }

    public double surfaceArea() {
        return 6 * length * length;
    }
}