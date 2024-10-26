package lab2.pr3;

public class Main {
	public static void main(String[]args) { 
		Bank bank = new Bank(); 
		Account acc1= new Account(1); 
		Savings  acc2= new Savings(2, 2.5); 
		CheckingAccount  acc3= new CheckingAccount(3);
		
		bank.openAcc(acc1);
		bank.openAcc(acc2);
		bank.openAcc(acc3);
		
		acc1.deposit(1000);
		acc2.deposit(2000);
		acc3.deposit(3000);
		
		bank.update();
		
		System.out.println("Acc1 balance: "+ acc1.getBalance());
		System.out.println("Acc2 balance: "+ acc2.getBalance());
		System.out.println("Acc3 balance: "+ acc3.getBalance());
		System.out.println(" ");
		
		
		acc1.withdraw(200);
		acc2 .withdraw(1000);
		acc3 .withdraw(2000); 
		bank.update();
		
		System.out.println("Acc1 balance: "+ acc1.getBalance());
		System.out.println("Acc2 balance: "+ acc2.getBalance());
		System.out.println("Acc3 balance: "+ acc3.getBalance());
		
	}
}
