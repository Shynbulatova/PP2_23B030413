package lab2.pr3;
import java.util.Vector; 
class Bank {
	private Vector<Account> accs; 
	
	
	public Bank() { 
		accs = new Vector<>(); 
	}
	
	public void openAcc(Account account) { 
		accs.add(account); 
	}
	
	public void closeAcc(Account account) { 
		accs.remove(account); 
	}
	
	public void update() { 
		for (Account account : accs){ 
			// Deposit or withdraw money from the account
            // Perform other necessary operations

            if (account instanceof Savings) { 
            	Savings savings = (Savings) account; 
            }
            else if (account instanceof CheckingAccount) { 
            	CheckingAccount checkingAccount= (CheckingAccount) account; 
            	checkingAccount.deductFee();
//			account.addInterest(); 
            }
		}
	}
}
