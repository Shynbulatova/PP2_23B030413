package Labs;
//3
public class Temperature {

    private double value;
    private char scale;

    public Temperature() {
        this(0, 'C');
    }

    public Temperature(double value) {
        this(value, 'C');
    }

    public Temperature(char scale) {
        this(0, scale);
    }

    public Temperature(double value, char scale) {
        this.value = value;
        this.scale = scale;
    }

    public double getCelsius() {
        if (scale == 'C') {
            return value;
        } else {
            return 5 * (value - 32) / 9;
        }
    }

    public double getFahrenheit() {
        if (scale == 'F') {
            return value;
        } else {
            return (9 * (value / 5)) + 32;
        }
    }

    public char getScale() {
        return scale;
    }

    public void setValue(double value) {
        this.value = value;
    }

    public void setScale(char scale) {
        this.scale = scale;
    }

    public void setTemperature(double value, char scale) {
        this.value = value;
        this.scale = scale;
    }

    public static void main(String[] args) {
        Temperature temp1 = new Temperature();
        Temperature temp2 = new Temperature(100, 'F');

        System.out.println("Temp1 in Celsius: " + temp1.getCelsius());
        System.out.println("Temp1 in Fahrenheit: " + temp1.getFahrenheit());

        System.out.println("Temp2 in Celsius: " + temp2.getCelsius());
        System.out.println("Temp2 in Fahrenheit: " + temp2.getFahrenheit());

        temp1.setTemperature(25, 'C');
        System.out.println("Temp1 updated in Celsius: " + temp1.getCelsius());
        System.out.println("Temp1 updated in Fahrenheit: " + temp1.getFahrenheit());
    }
}
