package task1;

public class Cylinder extends Shape3d{
    private double radius, height;
    public Cylinder(double r, double h) {
        this.radius = r;
        this.height = h;

    }

    public double volume() {
        return Math.PI * radius * height;
    }

    public double surfaceArea() {
        return Math.PI * radius * radius;
    }

}
