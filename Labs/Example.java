package Labs;
//2
public class Example {
	public enum OperatingSystem {
        WINDOWS, MACOS, LINUX
    }

    public static final int MAX_BATTERY_LEVEL = 100;
    private final String brand;
    private static int totalLaptops = 0;
    private int batteryLevel;
    private OperatingSystem os;

    {
        batteryLevel = 50;
        System.out.println("Laptop initialized with battery at " + batteryLevel + "%");
    }

    public Example(String brand, OperatingSystem os) {
        this.brand = brand;
        this.os = os;
        totalLaptops++;
    }

    public void charge() {
        charge(10);
    }

    public void charge(int amount) {
        if (this.batteryLevel + amount <= MAX_BATTERY_LEVEL) {
            this.batteryLevel += amount;
        } else {
            this.batteryLevel = MAX_BATTERY_LEVEL;
        }
        System.out.println("Battery charged to: " + this.batteryLevel + "%");
    }

    public OperatingSystem getOperatingSystem() {
        return os;
    }

    public static int getTotalLaptops() {
        return totalLaptops;
    }

    public final void displayInfo() {
        System.out.println("Brand: " + brand + ", OS: " + os + ", Battery: " + batteryLevel + "%");
    }

    public static void main(String[] args) {
        Laptop laptop1 = new Example("Dell", Example.OperatingSystem.WINDOWS);
        laptop1.charge();
        laptop1.charge(30);
        laptop1.displayInfo();

        Laptop laptop2 = new Example("Apple", Example.OperatingSystem.MACOS);
        laptop2.charge(20);
        laptop2.displayInfo();

        System.out.println("Total laptops created: " + Example.getTotalLaptops());
    }
    
}

