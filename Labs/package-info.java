package Labs;
import java.util.Scanner;
public class Data {
    private double sum;
    private double largest;
    private int count;

    // Конструктор
    public Data() {
        sum = 0;
        largest = Double.NEGATIVE_INFINITY;
        count = 0;
    }

    // Метод для добавления значения
    public void add(double value) {
        sum += value;
        if (value > largest) {
            largest = value;
        }
        count++;
    }

    // Метод для вычисления среднего значения
    public double getAverage() {
        if (count == 0) {
            return 0; // Если нет данных
        }
        return sum / count;
    }

    // Метод для нахождения самого большого значения
    public double getLargest() {
        return largest;
    }
}
