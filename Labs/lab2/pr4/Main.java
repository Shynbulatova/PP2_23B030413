package lab2.pr4;

import java.util.Scanner; 
public class Main {
    public static void main(String[] args) {
    	
    	
    	Circuit a = new Resistor(3.0); 
    	Circuit b = new Resistor(3.0); 
    	Circuit c = new Resistor(6.0); 
    	Circuit d = new Resistor(3.0); 
    	Circuit e = new Resistor(2.0); 
    	Circuit f = new Series(a, b); 
    	Circuit g = new Parallel(c, d); 
    	Circuit h = new Series(g ,e ); 
    	Circuit circuit = new Parallel(h, f); 
    	
    	

        double equivalentResistance = circuit.getResistance();
        System.out.println("Equivalent Resistance: " + equivalentResistance);
        
        
        
        Scanner s = new Scanner(System.in); 
        double voltage = s.nextDouble(); 
        double power = circuit.getPower(voltage, equivalentResistance); 
        System.out.println("Power: "+ power); 
        
    }
}
