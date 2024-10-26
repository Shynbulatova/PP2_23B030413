package lab2.pr3;

public class CheckingAccount  extends Account{
	private int cnt; 
	private static final int freeTransaction = 3; 
	private static final double transactionFee = 00.2;
	
	public CheckingAccount() { 
		
	}
	
	public CheckingAccount(int accNumber) { 
		super(accNumber);
		cnt =0; 
	}
	
	public void deductFee() { 
		if (cnt>freeTransaction) { 
			double fee = transactionFee * cnt; 
			withdraw(fee); 
		}
		
		cnt=0 ; // resetting cnt 
	}
	
	@Override
	public void deposit(double sum) { 
		super.deposit(sum);
		cnt++;
	}
	
	@Override
	public void withdraw(double sum) { 
		super.withdraw(sum);
		cnt++; 
	}
}	