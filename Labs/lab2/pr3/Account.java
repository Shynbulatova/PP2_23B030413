package lab2.pr3;

class Account {
	private double balance; 
	private int accNumber; 
	
	public Account() { 
	}
	
	public Account(int a) { 
		balance =0.0; 
		accNumber= a; 
	}
	
	public void deposit(double sum) { 
		balance += sum ;
	}
	
	public void withdraw(double sum) { 
		balance -= sum;
	}
	
	public double getBalance() { 
		return balance; 
	}
	
	public double getAccNumber() { 
		return accNumber; 
	}
	
	public String toString() { 
		return "balance "+ balance+ " accNumber "+ accNumber;
	}
	
	public final void print() { 
		System.out.println(toString()); 
	}
}
