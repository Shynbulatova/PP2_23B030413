package lab2.pr4;

public class Series extends Circuit {
    private Circuit circuit1;
    private Circuit circuit2;

    public Series(Circuit circuit1, Circuit circuit2) {
        this.circuit1 = circuit1;
        this.circuit2 = circuit2;
    }

    public double getResistance() {
        return circuit1.getResistance() + circuit2.getResistance();
    }
}
