package lab2.pr4;

public abstract class Circuit {
    public abstract double getResistance();
//    public abstract double getPotDiff(); 
//    public abstract void applyPotDiff(double V);
    
    public double getPower(double voltage , double resistance) { 
    	double power = Math.pow(voltage, 2 )/ resistance; 
    	return power; 
    	
    }
//    
//    public double getCurrent() {
//    	
//    }
//    
    
}
