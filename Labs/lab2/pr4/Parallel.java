package lab2.pr4;

public class Parallel extends Circuit {
    private Circuit circuit1;
    private Circuit circuit2;

    public Parallel(Circuit circuit1, Circuit circuit2) {
        this.circuit1 = circuit1;
        this.circuit2 = circuit2;
    }

    public double getResistance() {
        double resistance1 = circuit1.getResistance();
        double resistance2 = circuit2.getResistance();
        return 1 / ((1 / resistance1) + (1 / resistance2));
    }
}