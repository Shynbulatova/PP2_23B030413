package task1;
import java.util.Scanner;

public class Testt {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter radius and height for Cylinder:");
        double radius = scanner.nextDouble();
        double height = scanner.nextDouble();
        Cylinder cylinder = new Cylinder(radius, height);
        System.out.println("Cylinder Volume: " + cylinder.volume());
        System.out.println("Cylinder Surface Area: " + cylinder.surfaceArea());

        System.out.println("Enter radius for Sphere:");
        double radiusSphere = scanner.nextDouble();
        Sphere sphere = new Sphere(radiusSphere);
        System.out.println("Sphere Volume: " + sphere.volume());
        System.out.println("Sphere Surface Area: " + sphere.surfaceArea());

        System.out.println("Enter side length for Cube:");
        double length = scanner.nextDouble();
        Cube cube = new Cube(length);
        System.out.println("Cube Volume: " + cube.volume());
        System.out.println("Cube Surface Area: " + cube.surfaceArea());

        scanner.close();
    }
}