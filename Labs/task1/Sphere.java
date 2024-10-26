package task1;

public class Sphere extends Shape3d{
    //S = 4πr² V = (4/3)πr³
    private double radius;
    public Sphere(double r) {
        this.radius = r;


    }
    public double volume() {
        return Math.PI * Math.pow(radius, 3) * 4/3;
    }

    public double surfaceArea() {
        return Math.PI * radius * radius *4;
    }

}