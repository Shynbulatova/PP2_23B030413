package task1.b;
import java.util.Scanner;


public class Test {

 public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);
  String title = scanner.nextLine();
  String author = scanner.nextLine();
  Integer year = scanner.nextInt();
  Integer numberOfPages = scanner.nextInt();
  
  
  Book book = new Book(title, author, year, numberOfPages);
  System.out.println("Title of book: " + book.getTitle()) ;
  System.out.println("Author of book: " + book.getAuthor()) ;
  System.out.println("Publication year of book: " + book.getPublicationYear()) ;
  System.out.println("Number of pages:  " + book.getNumberOfPages()) ;
  
  scanner.close();

 }

}